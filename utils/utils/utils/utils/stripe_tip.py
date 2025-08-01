import stripe
import os

stripe.api_key = os.getenv("STRIPE_API_KEY")

def create_tip_checkout(amount):
    """
    Creates a Stripe checkout session for Dreamverse tips
    """
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': 'Dreamverse Tip'},
                'unit_amount': int(amount * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://dream-verse.co.uk/success',
        cancel_url='https://dream-verse.co.uk/cancel',
    )
    return session.url
