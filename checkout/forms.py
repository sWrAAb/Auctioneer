from django import forms
from .models import Order


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=True)
    cvc = forms.CharField(label='Security code (CVC)', required=True)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=True)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=True)
    #stripe_id = forms.CharField(widget=forms.HiddenInput)
    

    def clean(self):
        cleaned=super(MakePaymentForm,self).clean()
        if not self.errors: 
            credit_card_number=self.cleaned_data['credit_card_number']
            cvc=self.cleaned_data['cvc']
            expiry_month=self.cleaned_data['expiry_month']
            expiry_year=self.cleaned_data['expiry_year']
            stripe_id=self.cleaned_data['stripe_id']

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2',
            'county'
        )