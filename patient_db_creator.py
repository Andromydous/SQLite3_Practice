import csv
import sqlite3

connection = sqlite3.connect("patients.db")
cursor = connection.cursor()
create_table = """CREATE TABLE patient_attendance(
                patient_id INTEGER NOT NULL,
                gender TEXT NOT NULL,
                marital_status TEXT NOT NULL,
                city TEXT NOT NULL,
                state TEXT NOT NULL,
                zip_code INTEGER NOT NULL,
                age INTEGER NOT NULL,
                procedure TEXT NOT NULL,
                follow_up_attended TEXT NOT NULL);
                """

cursor.execute(create_table)

file = open("Scenario2.csv")
contents = csv.reader(file)

insert_records = "INSERT INTO patient_attendance (patient_id, gender, marital_status, city, state, zip_code, age, " \
                 "procedure, follow_up_attended) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(insert_records, contents)

select_all = "SELECT * FROM patient_attendance"
rows = cursor.execute(select_all).fetchall()

for row in rows:
    print(row)

connection.commit()
connection.close()