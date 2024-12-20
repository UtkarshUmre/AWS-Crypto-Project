from flask import Flask, render_template, request, redirect, url_for
import os
import sys

app = Flask(__name__)

# Load default credentials from environment variables
DEFAULT_USERNAME = os.getenv('DEFAULT_USERNAME')
DEFAULT_PASSWORD = os.getenv('DEFAULT_PASSWORD')

# Check if the credentials are set
if not DEFAULT_USERNAME or not DEFAULT_PASSWORD:
    print("Error: Please set the environment variables DEFAULT_USERNAME and DEFAULT_PASSWORD.")
    sys.exit(1)  # Exit the application if credentials are not set

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if provided credentials match the environment ones
        if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:
            return redirect(url_for('welcome'))
        else:
            error = 'Invalid Credentials. Please try again.'

    return render_template('login.html', error=error)

@app.route('/welcomepage')
def welcome():
    return render_template('product.html')

@app.route('/place_order')
def place_order():
    product_id = request.args.get('product')
    return render_template('place_order.html', product_id=product_id)

@app.route('/submit_order', methods=['POST'])
def submit_order():
    product_id = request.form['product_id']
    name = request.form['name']
    address = request.form['address']
    quantity = request.form['quantity']

    # Here you would process the order, e.g., save it to a database
    # and possibly prepare for payment processing

    return render_template('order_confirmation.html', name=name, product_id=product_id, quantity=quantity, address=address)

@app.route('/external_service')
def external_service():
    return render_template('external_service.html')
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
