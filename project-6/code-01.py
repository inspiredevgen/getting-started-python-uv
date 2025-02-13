import duckdb as db

def createCustomersdb():
    con = db.connect('customersdb.db')
    con.execute('''
    CREATE OR REPLACE TABLE customerdb(
        index VARCHAR,
        customer_id VARCHAR,
        first_name VARCHAR,
        last_name VARCHAR,
        company VARCHAR,
        city VARCHAR,
        country VARCHAR,
        phone_1 VARCHAR,
        phone_2 VARCHAR,
        email VARCHAR,
        subscription_date VARCHAR,
        Website VARCHAR
        );
    ''')
    return con

def loadData(con):

    con.sql('''
        INSERT INTO customerdb (index, customer_id, first_name, last_name, company, city, country, phone_1, phone_2, email, subscription_date, Website) 
        (SELECT * FROM "customers.csv")
        ''')
    con.sql('SELECT * FROM customerdb LIMIT 5;').show()

if __name__ == '__main__':
    db.read_csv('customers.csv')
    resultat = db.sql('SELECT * FROM "customers.csv"')
    dbschema = createCustomersdb()
    loadData(dbschema)