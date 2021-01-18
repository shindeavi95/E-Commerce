import json
from . models import *


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
        print(cart)
    except:
         cart = {}   
    items = []
    order = {"get_cart_items": 0, "get_cart_total": 0,"shipping":False}
    cartItems = order["get_cart_items"]

    for i in cart:
        # we use try block to prevent items in cart that may have been remove from
        try:
            cartItems += cart[i]['quantity']

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order["get_cart_total"] += total
            order["get_cart_items"] += cartItems

            item = {
                'product':{
                    'id':product.id,   # this is get from database
                    'name':product.name, # this is get from database
                    'price':product.price, # this is get from database
                    'imageURL':product.imageURL, # this is get from database
                },
                'quantity':cart[i]['quantity'], # this is get from Cookies
                'get_total':total       # this is get from Cookies
                }

            items.append(item)
            if product.digital == False:
                order["shipping"] = True    
        except:
            pass        
    return {'cartItems':cartItems,'order':order,'items':items}



def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
        items = order.orderitem_set.all()  # find out which method it is ?
    else:
        cookieData = cookieCart(request)
        order = cookieData['order']
        cartItems = cookieData['cartItems']
        items = cookieData['items']
    return {'order':order,'cartItems':cartItems,'items':items}



def guestOrder(request, data):
    print('User is not logged in...')  
    print('COOKIES:', request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
        email=email,
    )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )
    for item in items:
        product = Product.objects.get(id=item['product']['id'])

        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )
    return customer, order    