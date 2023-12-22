"""
URL configuration for restoran project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from restaurant.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('user/', user, name='user'),
    path('user/tambah_user/', tambah_user, name='tambah_user'),
    path('user/ubah/<int:id_user>', ubah_user, name='ubah_user'),
    path('user/hapus/<int:id_user>', hapus_user, name='hapus_user'),
    
    path('table/', table, name='table'),
    path('table/tambah_table/', tambah_table, name='tambah_table'),
    path('table/ubah/<int:id_table>', ubah_table, name='ubah_table'),
    path('table/hapus/<int:id_table>', hapus_table, name='hapus_table'),
    
    path('menu/', menu, name='menu'),
    path('menu/tambah_menu/', tambah_menu, name='tambah_menu'),
    path('menu/ubah/<int:id_menu>', ubah_menu, name='ubah_menu'),
    path('menu/hapus/<int:id_menu>', hapus_menu, name='hapus_menu'),
    
    path('formula/', formula, name='formula'),
    path('formula/tambah_formula/', tambah_formula, name='tambah_formula'),
    path('formula/ubah/<int:id_formula>', ubah_formula, name='ubah_formula'),
    path('formula/hapus/<int:id_formula>', hapus_formula, name='hapus_formula'),
    
    path('order/', order, name='order'),
    path('order/tambah_order/', tambah_order, name='tambah_order'),
    path('order/ubah/<int:id_order>', ubah_order, name='ubah_order'),
    path('order/hapus/<int:id_order>', hapus_order, name='hapus_order'),
]
