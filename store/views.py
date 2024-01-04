from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.

#------------------------------------------------PAGES----------------------------------------

def store(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'store/store.html',context)

def cart(request):

    if request.user.is_authenticated:
        customer=request.user.customer
        order, created =Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_CartTotal':0,'get_CartItems':0}
    context={'items':items,'order':order}
    return render(request,"store/cart.html",context)

def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created =Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_CartTotal':0,'get_CartItems':0}
    context={'items':items,'order':order}
    return render(request,"store/checkout.html",context)

#------------------------------------------------ADD TO CART----------------------------------------------

def updateItem(request):
    return JsonResponse('Item was added',safe=False)


