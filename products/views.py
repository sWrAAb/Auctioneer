from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, "products.html", {"products": products})



