import duckdb as db

def simpleQuery():
    rel = db.sql("SELECT * FROM range(10) AS tbl(Numbers)")
    rel.show()

def dbConnect():
    # Create / connect to database
    con = db.connect('sampledb.db')
    con.sql('SHOW ALL TABLES').show()

def vehiclesDB():
    con = db.connect('vehiclesdb.db')
    con.execute('''
    CREATE OR REPLACE TABLE vehicles(
        car_id INTEGER,
        brand VARCHAR,
        model VARCHAR,
        year INTEGER,
        city VARCHAR,
        state VARCHAR
    );
    ''')

    # Insert some data
    con.execute('''
    INSERT INTO vehicles VALUES
    (1, 'Tesla', 'Model Y', 2024, 'Toronto', 'ON'),
    (2, 'Mercedes-Benz', 'GLE', 2022, 'Montreal', 'QC'),
    (3, 'Nissan', 'Murano', 2019, 'Vancouver', 'BC'),
    (4, 'Toyota', 'Rav4', 2015, 'Calgary', 'AB'),
    (5, 'Ford', 'Explorer', 2022, 'Oakville', 'ON');
    ''')

    con.sql('SELECT * FROM vehicles').show()

def main():
    #simpleQuery()

    #dbConnect()

    vehiclesDB()

if __name__ == "__main__":
    main()
