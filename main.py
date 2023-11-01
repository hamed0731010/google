from pymongo import MongoClient
import sqlite3
from fastapi import FastAPI
from uvicorn import run
import psycopg2
from images import get_images_link
# Database connection parameters
db_params = {
    'host': 'localhost',  # or use the IP address of your Docker host
    'database': 'psq',
    'user': 'postgres',
    'password': 'asdzxc',
}

# Connect to the PostgreSQL database
connection = psycopg2.connect(**db_params)

# Create a cursor object
cursor = connection.cursor()

# Execute SQL queries here
# SQL command to create a new table

# Create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS new (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT
);
'''
cursor.execute(create_table_query)

# Insert data into the table
insert_data_query = '''
INSERT INTO new (name, age)
VALUES (%s, %s);
'''

data_to_insert = [
    ('Alice', 25),
    ('Bob', 30),
    ('Charlie', 22)
]

for data in data_to_insert:
    cursor.execute(insert_data_query, data)

# Commit changes
connection.commit()

# Close the cursor and connection when done
cursor.close()
connection.close()