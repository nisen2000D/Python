from django.shortcuts import render

# Create your views here.
from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.urls import reverse_lazy
from mainapp.models import Product, ProductCategory
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from adminapp.forms import ProductEditForm
from django.views.generic.detail import DetailView


class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'
        return context



class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    fields = '__all__'
    success_url = reverse_lazy('adminapp:categories')
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'
        context['title_submenu'] = 'Создание категории'
        return context



class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    fields = '__all__'
    success_url = reverse_lazy('adminapp:categories')
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'
        context['title_submenu'] = 'Изменение категории'
        return context


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:categories')
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории'
        context['title_submenu'] = 'Удаление категории'
        return context


class ProductView(ListView):
    model = Product
    template_name = 'adminapp/products.html'
    #queryset = Product.objects.filter(category__pk=kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукты'
        if self.kwargs['pk'] == 0:
            category = {'pk': 0}
        else:
            category = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
        context['category'] = category
        return context

    def get_queryset(self):
        if self.kwargs['pk'] == 0:
            return Product.objects.all()
        return Product.objects.filter(category__pk=self.kwargs['pk'])

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/products.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    fields = '__all__'
    #success_url = reverse_lazy('adminapp:products')
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукты'
        context['title_submenu'] = 'Создание товара'
        #category = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
        context['pk'] = self.kwargs['pk']
        return context
    
    def get_success_url(self):
        return reverse_lazy('adminapp:products',  kwargs={'pk': self.kwargs['pk']})


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    fields = '__all__'
    success_url = reverse_lazy('adminapp:products')
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('adminapp:products',  kwargs={'pk': 0})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукты'
        context['title_submenu'] = 'Редактирование товара'
        category = {'pk': 0}
        context['category'] = category
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_update.html'
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('adminapp:products',  kwargs={'pk': 0})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукты'
        context['title_submenu'] = 'Удаление товара'
        category = {'pk': 0}
        context['category'] = category
        return context


class UserListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователи'
        return context


class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    fields = '__all__'
    success_url = reverse_lazy('adminapp:users')
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователи'
        context['title_submenu'] = 'Создание пользователя'
        return context


class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    fields = '__all__'
    success_url = reverse_lazy('adminapp:users')
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователи'
        context['title_submenu'] = 'Обновление пользователя'
        return context

class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('adminapp:users')
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователи'
        context['title_submenu'] = 'Удаление пользователя'
        return context

    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(ShopUser, pk=kwargs['pk'])
        user.is_active = False
        user.save()
        return HttpResponseRedirect(self.success_url)


def product_read(request, pk):
    title = 'продукт/подробнее'
    product = get_object_or_404(Product, pk=pk)
    content = {'title': title, 'object': product, }

    return render(request, 'adminapp/product_read.html', content)


def product_create(request, pk):
    title = 'продукт/создание'
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})
        content = {'title': title,
                   'update_form': product_form,
                   'category': category
                   }

        return render(request, 'adminapp/product_update.html', content)

    def product_update(request, pk):
        title = 'продукт/редактирование'

        edit_product = get_object_or_404(Product, pk=pk)

        if request.method == 'POST':
            edit_form = ProductEditForm(request.POST, request.FILES, \
                                                                    instance=edit_product)
            if edit_form.is_valid():
                edit_form.save()
                return HttpResponseRedirect(reverse('admin:product_update', \
                                                                           args=[edit_product.pk]))
        else:
            edit_form = ProductEditForm(instance=edit_product)

        content = {'title': title,
                   'update_form': edit_form,
                   'category': edit_product.category
                   }

        return render(request, 'adminapp/product_update.html', content)

    def product_delete(request, pk):
        title = 'продукт/удаление'

        product = get_object_or_404(Product, pk=pk)

        if request.method == 'POST':
            product.is_active = False
            product.save()
            return HttpResponseRedirect(reverse('admin:products', \
                                                                 args=[product.category.pk]))

        content = {'title': title, 'product_to_delete': product}

        return render(request, 'adminapp/product_delete.html', content)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'