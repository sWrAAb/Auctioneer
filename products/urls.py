from django.urls import path
from .views import (
    all_products,
    HomeView,
    ProductDetailView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='products'),
    path('<slug>', ProductDetailView, name='product')
]