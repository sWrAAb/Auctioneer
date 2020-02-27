from django.urls import path, include
from .views import (
    all_products,
    HomeView,
    ProductDetailView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='products'),
    path('product/<slug>', ProductDetailView, name='product')
]