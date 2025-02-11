import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.exceptions import abort
import datetime

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

app.config['SECRET_KEY'] = 'your secret key'

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

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        m_year = request.form['m_year']
        color = request.form['color']
        province = request.form['province']
        city = request.form['city']

        if not brand:
            flash('brand is required!')
        elif not model:
            flash('model is required!')
        elif not m_year:
            flash('year is required!')
        else:
            conn = get_db_connection()

            conn.execute('INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)',
                        (brand, model, m_year, color, province, city))

            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    car = get_car(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM cars WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(car['brand']))
    return redirect(url_for('index'))

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    currentDateTime = datetime.datetime.now()
    car = get_car(id)

    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        m_year = request.form['m_year']
        color = request.form['color']
        province = request.form['province']
        city = request.form['city']

        if not brand:
            flash('Brand is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE cars SET created = ?, brand = ?, model = ?, m_year = ?, color = ?, province = ?, city = ?'
                         ' WHERE id = ?',
                        (currentDateTime, brand, model, m_year, color, province, city, id))

            conn.commit()
            conn.close()
            msg = f"{brand} {model} was successfully updated!"
            return redirect(url_for('index'))

    return render_template('edit.html', car=car)
