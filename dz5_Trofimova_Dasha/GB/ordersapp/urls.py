"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import ordersapp.views as ordersapp
from django.urls import re_path

app_name="ordersapp"

urlpatterns = [
   re_path(r'^$', ordersapp.OrderList.as_view(), name='orders_list'),
   re_path(r'^forming/complete/(?P<pk>\d+)/$',
           ordersapp.order_forming_complete, name='order_forming_complete'),
   re_path(r'^create/$', ordersapp.OrderCreate.as_view(),
           name='order_create'),
   re_path(r'^read/(?P<pk>\d+)/$', ordersapp.OrderRead.as_view(),
           name='order_read'),
   re_path(r'^update/(?P<pk>\d+)/$', ordersapp.OrderCreate.as_view(),
           name='order_update'),
   re_path(r'^delete/(?P<pk>\d+)/$', ordersapp.OrderDelete.as_view(),
           name='order_delete'),
]
