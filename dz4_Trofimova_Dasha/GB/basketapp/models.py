from django.contrib.auth import get_user_model
from django.db import models

from mainapp.models import Product


class BasketQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class BasketItem(models.Model):
    # objects = BasketQuerySet.as_manager()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    def delete(self):
        self.product.quantity += self.quantity
        self.product.save()
        super(self.__class__, self).delete()

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - \
                                     self.__class__.get_item(self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super(self.__class__, self).save(*args, **kwargs)

    @classmethod
    def get_item(cls, pk):
        return cls.objects.filter(pk=pk).first()

class Basket(models.Model):
   ...
   # переопределяем метод, сохранения объекта
   def save(self, *args, **kwargs):
       if self.pk:
           self.product.quantity -= self.quantity - \
                                    self.__class__.get_item(self.pk).quantity
       else:
           self.product.quantity -= self.quantity
       self.product.save()
       super(self.__class__, self).save(*args, **kwargs)