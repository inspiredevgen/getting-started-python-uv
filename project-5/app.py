import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort

db_connection_string="db/cars.db"

def get_db_connection():
    conn = sqlite3.connect(db_connection_string)
    conn.row_factory = sqlite3.Row
    return conn

def get_car(car_id):
    conn = get_db_connection()
    car = conn.execute('SELECT * FROM cars WHERE id = ?',
                        (car_id,)).fetchone()
    conn.close()
    if car is None:
        abort(404)
    return car

app = Flask(__name__)


@app.route('/')
def index():
    conn = get_db_connection()
    cars = conn.execute('SELECT * FROM cars').fetchall()
    conn.close()
    return render_template('index.html', cars=cars)

@app.route('/<int:car_id>')
def car(car_id):
    car = get_car(car_id)
    return render_template('car.html', car=car)
