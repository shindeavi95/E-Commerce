from django.shortcuts import render
from store.models import *


def store(request):
    products = Product.objects.all()
    return render(request, "store/store.html", {"products": products})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()  # find out which method it is ?
    else:
        items = []
        order = {"get_cart_items": 0, "get_cart_total": 0}
    context = {"items": items, "order": order}
    return render(request, "store/cart.html", context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()  # find out which method it is ?
    else:
        items = []
        order = {"get_cart_items": 0, "get_cart_total": 0}
    context = {"items": items, "order": order}
    return render(request, "store/checkout.html", context)
