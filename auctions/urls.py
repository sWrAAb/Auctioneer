from django.urls import path
from .views import (
    all_auctions,
    HomeView
)

urlpatterns = [
    path('', HomeView.as_view(), name='auctions'),
]