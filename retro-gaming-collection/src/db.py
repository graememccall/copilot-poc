from flask import Flask
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# Database configuration
app.config['MYSQL_HOST'] = os.getenv('DB_HOST')
app.config['MYSQL_USER'] = os.getenv('DB_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('DB_NAME')

mysql = MySQL(app)

def get_db_connection():
    return mysql.connection

def close_db_connection(conn):
    conn.close()