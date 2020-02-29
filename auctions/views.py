from django.shortcuts import render
from django.views.generic import ListView
from .models import Auction

# Create your views here.
def all_auctions(request):
    auctions = Auction.objects.all()
    return render(request, "auctions.html", {"auctions": auctions})


def auctions(request):
    context = {
        'auctions': Auction.Object.all
    }
    return render(request, 'auctions.html, context')


class HomeView(ListView):
    model = Auction
    template_name = "auctions.html"
