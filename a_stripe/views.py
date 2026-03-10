from django.conf import settings
from django.shortcuts import render
import stripe

stripe.api_key=settings.STRIPE_SECRET_KEY

# Create your views here.
def product_view(request):
    print(settings.STRIPE_SECRET_KEY,'stripekey-------------')
    product_id='prod_U7KAlIY8A70VXy'
    product=stripe.Product.retrieve(product_id)
    print(product,"99999999999999")
    prices=stripe.Price.list(product=product_id)
    price=prices.data[0]
    product_price=price.unit_amount / 100.0
    return render(request,"a_stripe/product.html",{'product':product,"product_price":product_price})