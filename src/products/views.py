from django.shortcuts import render

def ProductDetailView(request, slug, *args, **kwargs):
    template = "product.html"
    context = {

    }

    return render(request, template, context)