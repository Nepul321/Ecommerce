from django.shortcuts import redirect, render
from products.models import Product


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