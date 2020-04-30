from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method=="POST":
        #import pdb; pdb.set_trace()
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        customer = ''
        
        if  True:
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order, 
                    product = product, 
                    quantity = quantity
                    )
                order_line_item.save()
                
            try:
                credit_card_number = request.POST.get('credit_card_number')
                expiry_month = request.POST.get('expiry_month')
                expiry_year = request.POST.get('expiry_year')
                cvc = request.POST.get('cvc')
                token = stripe.Token.create(
                    card = {
                        'number': credit_card_number,
                        'exp_month': int(expiry_month),
                        'exp_year': int(expiry_year),
                        'cvc': cvc
                    }
                )
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    source = token,
                    description = request.user.email,
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})

            if customer:

                if customer.paid:
                    messages.error(request, "You have successfully paid")
                    request.session['cart'] = {}
                    return redirect(reverse('products'))
                else:
                    messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
                
        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})