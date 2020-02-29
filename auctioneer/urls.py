"""auctioneer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from accounts.views import index, logout, login, registration, user_profile
from products.views import all_products, ProductDetailView
from auctions.views import all_auctions
from bidding.views import view_bidding
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('search/', include('search.urls')),
    path('checkout/', include('checkout.urls')),
    path('auctions/', include('auctions.urls')),
    path('bidding/', include('bidding.urls'))

]

# In debug mode

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)