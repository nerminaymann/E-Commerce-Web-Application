from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #LEAVE AS EMPTY STRING FOR BASE URL
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('update_item',views.updateItem,name='update_item')

]