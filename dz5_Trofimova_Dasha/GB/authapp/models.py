from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver

from shop import settings
from shop.settings import USER_EXPIRES_TIMEDELTA


def get_activation_key_expires():
    return now() + USER_EXPIRES_TIMEDELTA


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', null=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=get_activation_key_expires)

    def is_activation_key_expired(self):
        return now() > self.activation_key_expires

    @cached_property
    def basket_items(self):
        return self.user_basket.all()

    def basket_cost(self):
        return sum(item.product.price * item.quantity for item in self.basket_items)

    def basket_total_quantity(self):
        return sum(item.quantity for item in self.basket_items)

    def send_verify_mail(self):
        verify_link = reverse('auth:verify', kwargs={
            'email': self.email,
            'activation_key': self.activation_key,
        })

        title = f'Подтверждение учетной записи {self.username}'

        message = f'Для подтверждения учетной записи {self.username} на портале' \
                  f'{settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'

        return self.email_user(
            title, message, settings.EMAIL_HOST_USER, fail_silently=False)

    class Meta:
        ordering = ['-is_active', '-is_superuser', '-is_staff', 'username']


class ShopClientProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    user = models.OneToOneField(ShopUser, primary_key=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='теги', max_length=128, blank=True)
    aboutMe = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)
    langs = models.CharField(verbose_name='язык', blank=True, null=True, max_length=10)


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    user = models.OneToOneField(ShopUser, unique=True, null=False,\
                                db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='теги', max_length=128, \
                               blank=True)
    aboutMe = models.TextField(verbose_name='о себе', max_length=512, \
                               blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, \
                              choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)


    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()