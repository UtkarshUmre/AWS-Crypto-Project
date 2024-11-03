from flask import Flask, request, redirect, url_for, render_template
import psycopg2
import logging
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# RDS database configuration using environment variables
db_host = os.getenv('DB_HOST', 'default_host')
db_port = os.getenv('DB_PORT', '5432')
db_user = os.getenv('DB_USER', 'default_user')
db_password = os.getenv('DB_PASSWORD', 'default_password')
db_name = os.getenv('DB_NAME', 'default_db')
table_name = 'users'

# Database Connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=db_name, 
            user=db_user, 
            password=db_password, 
            host=db_host
        )
        logging.debug("Database connection successful.")
        return conn
    except Exception as e:
        logging.debug(f"Database connection failed: {e}")
        return None

# Routes
@app.route('/welcome')
def login():
    return render_template('login.html')

@app.route('/')
def home():
    return "Hello, this is the home page."

@app.route('/welcome/login', methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            return redirect(url_for('product'))
    
    return redirect(url_for('login'))

@app.route('/welcome/product')
def product():
    return redirect("http://crypto-app-882103207.eu-central-1.elb.amazonaws.com:5000/welcomepage")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
