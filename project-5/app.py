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


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_car(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(car['brand']))
    return redirect(url_for('index'))

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_car(id)

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
            conn.execute('UPDATE cars SET brand = ?, model = ?, m_year = ?, color = ?, province = ?, city = ?'
                         ' WHERE id = ?',
                         (brand, model, m_year, color, province, city, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)
