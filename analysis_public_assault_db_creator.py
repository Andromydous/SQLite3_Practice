import csv
import sqlite3

connection = sqlite3.connect("analysis-public-place-assaults-sexual-assaults-and-robberies-2015.db")
cursor = connection.cursor()
create_table = """CREATE TABLE public_assaults_and_robberies_2015(
                ID INTEGER NOT NULL, 
                Area_unit_2013_code INTEGER NOT NULL, 
                Area_unit_2013_label TEXT NOT NULL, 
                Victimisations_calendar_year_2015 INTEGER NOT NULL, 
                Population_mid_point_2015 INTEGER NOT NULL, 
                Rate_per_10000_population INTEGER NOT NULL, 
                Rate_ratio_NZ_average_rate INTEGER NOT NULL, 
                Urban_area_2013_code INTEGER NOT NULL, 
                Urban_area_2013_label TEXT NOT NULL, 
                Urban_area_type TEXT NOT NULL, 
                Territorial_authority_area_2013_code INTEGER NOT NULL, 
                Territorial_authority_area_2013_label TEXT NOT NULL, 
                Region_2013_code INTEGER NOT NULL, 
                Region_2013_label TEXT NOT NULL);
                """

cursor.execute(create_table)

file = open("analysis-public-place-assaults-sexual-assaults-and-robberies-2015-csv.csv")
contents = csv.reader(file)

insert_records = "INSERT INTO public_assaults_and_robberies_2015 (ID, Area_unit_2013_code, " \
                 "Area_unit_2013_label, Victimisations_calendar_year_2015, Population_mid_point_2015, " \
                 "Rate_per_10000_population, Rate_ratio_NZ_average_rate, Urban_area_2013_code, Urban_area_2013_label, " \
                 "Urban_area_type, Territorial_authority_area_2013_code, Territorial_authority_area_2013_label, " \
                 "Region_2013_code, Region_2013_label) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(insert_records, contents)

select_all = "SELECT * FROM public_assaults_and_robberies_2015"
rows = cursor.execute(select_all).fetchall()

for row in rows:
    print(row)

connection.commit()
connection.close()