from django.shortcuts import render

# Create your views here.

def view_bidding(request):
    """A View that renders the cart contents page"""
    return render(request, "bidding.html")