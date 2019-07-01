from flask import Flask, render_template, request
import stripe
import config

stripe_keys = {
    'secret_key': config.SECRET_KEY,
    'publishable_key': config.PUBLISHABLE_KEY
}

stripe.apu_key = stripe_keys['secret_key']

app = Flask (__name__)

@app.route('/charge', methods=['POST'])
def charge():
    amount = 500

    customer = stripe.Customer.create(
        email='customer@example.com',
        source=request.form['stripeToken']
        )
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )


def home():
    return render_template('home.htm', key = stripe_keys[])

if __name__== "__main__":
    app.run(debug=True)