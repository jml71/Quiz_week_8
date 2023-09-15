import sqlite3

conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

years = []
temperatures = []

cursor.execute('SELECT year, temperature FROM climate_data')
data = cursor.fetchall()

for row in data:
    year, temperature = row
    years.append(year)
    temperatures.append(temperature)

conn.close()
