import sqlite3
from flask import Flask, render_template
db_connection_string="db/cars.db"

def get_db_connection():
    conn = sqlite3.connect(db_connection_string)
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)


@app.route('/')
def index():
    conn = get_db_connection()
    cars = conn.execute('SELECT * FROM cars').fetchall()
    conn.close()
    return render_template('index.html', cars=cars)