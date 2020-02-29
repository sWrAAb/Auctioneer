from django.urls import path
from .views import view_bidding

urlpatterns = [
    path('', view_bidding, name='bidding'),
]

