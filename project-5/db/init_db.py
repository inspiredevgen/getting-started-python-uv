import sqlite3
connection = sqlite3.connect('cars.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Toyota", "Camry", 2020, "black", "Ontario", "Toronto"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Mercedes-Benz", "GLE", 2023, "red", "Quebec", "Montreal"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("BMW", "320i", 2015, "white", "Alberta", "Calgary"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Audi", "Q5", 2013, "black", "Ontario", "Toronto"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Toyota", "Corolla", 2022, "blue", "Ontario", "Kingston"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Ford", "Edge", 2021, "silver", "Quebec", "Montreal"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Ford", "Broncos", 2017, "black", "Ontario", "Burlington"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Audi", "eTron Q4", 2018, "white", "Alberta", "Calgary"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Toyota", "Rav4", 2017, "silver", "Manitoba", "Winnipeg"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Ford", "Explorer", 2018, "silver", "Ontario", "Oshawa"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Wolkswagen", "Tiguan", 2023, "blue", "Ontario", "Toronto"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Crysler", "Pacifica", 2021, "black", "Quebec", "Laval"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Toyota", "Rav4", 2020, "red", "Quebec", "Montreal"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Mitshubishi", "Outlander", 2020, "black", "Ontario", "Oakville"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Nissan", "Sentra", 2017, "silver", "Ontario", "Toronto"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Ford", "Mustang", 2018, "white", "Alberta", "Calgary"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Wolkswagen", "Atlas", 2020, "silver", "Ontario", "Toronto"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Toyota", "Camry", 2023, "white", "Ontario", "Oakville"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Acura", "RDX", 2021, "white", "Ontario", "Scarborough"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Honda", "Civic", 2024, "black", "Quebec", "Montreal"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Cadillac", "Escalade", 2024, "silver", "Manitoba", "Winnipeg"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Tesla", "Model 3", 2025, "silver", "Alberta", "Calgary"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Tesla", "Model Y", 2023, "blue", "Ontario", "Oshawa"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Toyota", "Rav4", 2021, "blue", "Ontario", "Scarborough"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Honda", "Pilot", 2020, "red", "Ontario", "Toronto"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Acura", "MDX", 2017, "blue", "Ontario", "Kingston"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Toyota", "Corolla", 2017, "blue", "Alberta", "Calgary"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Toyota", "Highlander", 2018, "red", "Quebec", "Montreal"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Hyundai", "Pallisade", 2023, "blue", "Alberta", "Edmonton"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Mercedes-Benz", "S350", 2020, "silver", "Ontario", "Toronto"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Tesla", "Model S", 2021, "black", "Quebec", "Laval"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Toyota", "Corolla", 2022, "white", "Ontario", "Mississauga"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Nissan", "Sentra", 2021, "black", "Alberta", "Calgary"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Hyundai", "Tucson", 2023, "silver", "British Columbia", "Vancouver"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Kia", "Telluride", 2024, "blue", "Ontario", "Scarborough"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Nissan", "Murano", 2020, "red", "Ontario", "Toronto"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Honda", "Civic", 2019, "red", "Manitoba", "Winnipeg"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Hyundai", "SantaFe", 2023, "red", "Quebec", "Montreal"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Hyundai", "iOniq", 2024, "blue", "Alberta", "Calgary"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Tesla", "Model 3", 2021, "blue", "Ontario", "Toronto"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Nissan", "Rogue", 2022, "black", "Ontario", "Ottawa"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Tesla", "Cybertruck", 2024, "silver", "Ontario", "Toronto"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Dodge", "Durango", 2017, "silver", "Ontario", "Kingston"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Hyundai", "SantaFe", 2019, "silver", "Quebec", "Montreal"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Nissan", "Pathfinder", 2020, "blue", "Ontario", "Toronto"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Honda", "CRV", 2021, "red", "Ontario", "Ottawa"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Tesla", "Model Y", 2022, "red", "Ontario", "Toronto"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Dodge", "Challenger", 2017, "white", "Ontario", "Mississauga"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Cadillac", "Lyriq", 2023, "white", "Ontario", "Kingston"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Tesla", "Model S Plaid", 2015, "silver", "Quebec", "Montreal"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Kia", "Sportage", 2016, "black", "Ontario", "Toronto"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Nissan", "Altima", 2015, "blue", "Ontario", "Toronto"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Mazda", "cz30", 2022, "blue", "Quebec", "Laval"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Volvo", "xc90", 2021, "red", "Ontario", "Kingston"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Kia", "ev9", 2025, "red", "Alberta", "Edmonton"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Tesla", "Model X", 2024, "white", "Ontario", "Ottawa"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Hyundai", "Elantra", 2017, "white", "Manitoba", "Winnipeg"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Hyundai", "Sonata", 2025, "black", "Ontario", "Ottawa"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Mercedes-Benz", "GLA", 2020, "black", "Alberta", "Edmonton"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Mercedes-Benz", "E Class", 2018, "blue", "Quebec", "Laval"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Lexus", "RX 350", 2023, "silver", "Ontario", "Ottawa"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Infiniti", "QX60", 2017, "white", "Ontario", "Toronto"))

cur.execute("INSERT INTO cars (brand, model, m_year, color, province, city) VALUES (?, ?, ?, ?, ?, ?)",
            ("Hyundai", "Tucson", 2021, "black", "British Columbia", "Vancouver"))


connection.commit()
connection.close()