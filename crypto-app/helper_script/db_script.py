import psycopg2
import sys
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Database connection info
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
db_port = os.getenv("DB_PORT", "5432")  # Default to PostgreSQL port

def create_table_clear_and_insert_default():
    # Connect to the database
    try:
        conn = psycopg2.connect(
            host=db_host,
            dbname=db_name,
            user=db_user,
            password=db_password,
            port=db_port
        )
        cursor = conn.cursor()

        # Create table query
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        );
        '''

        # Execute the query to create table
        cursor.execute(create_table_query)

        # Delete any existing data in the table
        delete_query = "DELETE FROM users;"
        cursor.execute(delete_query)

        # Insert default user
        insert_query = "INSERT INTO users (username, password) VALUES ('user', 'user');"
        cursor.execute(insert_query)

        conn.commit()
        print("Table created successfully, existing data cleared, and default user added.")

        # Query to get table information
        cursor.execute("SELECT column_name, data_type, character_maximum_length FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'users'")
        table_info = cursor.fetchall()
        print("\nTable Structure:")
        for column in table_info:
            print(f"Column Name: {column[0]}, Type: {column[1]}, Max Length: {column[2]}")

        # Query to print the data in the table
        cursor.execute("SELECT * FROM users")
        users_data = cursor.fetchall()
        print("\nData in 'users' Table:")
        for row in users_data:
            print(f"ID: {row[0]}, Username: {row[1]}, Password: {row[2]}")

    except Exception as e:
        print(f"Error connecting to the database: {e}")
        sys.exit(1)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Run the function
if __name__ == "__main__":
    create_table_clear_and_insert_default()
