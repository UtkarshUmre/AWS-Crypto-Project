import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variables for database connection
db_host = os.environ.get('AWS_RDS_URL')
db_port = os.environ.get('AWS_RDS_PORT')
db_user = os.environ.get('AWS_RDS_USERNAME')
db_password = os.environ.get('AWS_RDS_PASSWORD')
db_name = os.environ.get('AWS_RDS_DB_NAME')
table_name = 'users'

# Connect to the database
conn = psycopg2.connect(
    host=db_host,
    dbname=db_name,
    user=db_user,
    password=db_password,
    port=db_port
)
cur = conn.cursor()

# Create table
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
)
''')

# Insert dummy data
dummy_users = [
    ('Alice_dummy', 'alice_dummy@example.com', 'password123_dummy'),
    ('Bob_dummy', 'bob_dummy@example.com', 'password456_dummy'),
    ('Charlie_dummy', 'charlie_dummy@example.com', 'password789_dummy')
]

for user in dummy_users:
    cur.execute('''
    INSERT INTO users (name, email, password) VALUES (%s, %s, %s)
    ''', user)

conn.commit()

# Close the connection
cur.close()
conn.close()
