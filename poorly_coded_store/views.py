from django.shortcuts import render, redirect
from .models import Order, Product
from django.db.models import Sum


def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context) 



def pay(request):
    product_id =request.POST['product_id']
    quantity = request.POST['quantity']
    
    product = Product.objects.get(id=product_id)
    price = product.price
    
    total = price * int(quantity)
    
    Order.objects.create(quantity_ordered=quantity, total_price=total)
    
    return redirect('poorly_coded_store:checkout',quantity=int(quantity), price=int(price))


def checkout(request, quantity, price): 
    total_order_price = price * quantity

    orders_count = Order.objects.all().count()
    total_sum = Order.objects.aggregate(total_price=Sum('total_price'))['total_price']

    context={
        'total_order_price': total_order_price,
        'orders_count': orders_count,
        'total_sum':total_sum
    }
    
    return render(request, "store/checkout.html", context)