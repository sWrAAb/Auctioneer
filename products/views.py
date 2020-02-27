from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def products(request):
    context = {
        'products': Product.Object.all
    }
    return render(request, 'products.html, context')


class HomeView(ListView):
    model = Product
    template_name = "products.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"