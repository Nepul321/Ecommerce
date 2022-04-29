from django.shortcuts import redirect, render
from products.models import Product
from orders.models import Order, OrderItem
from django.contrib.auth.decorators import login_required


def HomeView(request, *args, **kwargs):
    template = "home.html"
    context = {

    }

    return render(request, template, context)

def ProductView(request, id, *args, **kwargs):
    template = "products/details.html"
    qs = Product.objects.filter(id=id)
    if not qs:
        return redirect('/')
    obj = qs.first()
    context = {
       'obj' : obj
    }

    return render(request, template, context)

@login_required
def CartView(request, *args, **kwargs):
    template = "cart/cart.html"
    user = request.user
    order, created = Order.objects.get_or_create(customer=user, complete=False)
    items = order.orderitem_set.all()
    context = {
      "items" : items,
      "order" : order
    }

    return render(request, template, context)