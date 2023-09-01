import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="report_email",
    user="fionawiggins",
    password="Skint962",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM birds")

print(cursor.fetchall())