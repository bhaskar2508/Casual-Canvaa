"""
URL configuration for canva_pro project.

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
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home),  
    path('register',v.register,name='register'),
    path('login',v.login_view,name='login'),
    path('logout',v.logout_view,name='logout'),
    path('collections',v.collections,name='Collections'),
    path('mlist',v.men_list,name='mlist'),
    path('add_to_cart/<int:pid>',v.add_to_cart,name='add_to_cart'),
    path('clist',v.cart_list,name='clist'),
    path('wlist',v.women_list,name='wlist'),
    path('contact',v.contact,name='contact'),
    path('add_to_cart_01/<int:wid>',v.women,name='add_to_cart_01'),
    path('klist',v.kids_list,name='klist'),
    path('add_to_cart_02/<int:kid>',v.kids,name='add_to_cart_02'),
    path('delete1',v.delete,name='delete1'),
    path('delete2',v.women_delete,name='delete2'),
    path('delete3',v.kid_delete,name='delete3'),
    path('elist',v.end_sale_list,name='elist'),
    path('add_to_cart_03/<int:lid>',v.endsale,name='add_to_cart_03'),
    path('delete4',v.endsale_delete,name='delete4'),
    path('about',v.about,name='about'),
    path('payment',v.payment_view,name='payment'),
    path('data1',v.data1,name='data1'),
    path('process_payment',v.process_payment,name='process_payment'),
]
