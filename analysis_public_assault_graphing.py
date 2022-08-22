import sqlite3
import pandas as pd
import matplotlib

connection = sqlite3.connect("analysis-public-place-assaults-sexual-assaults-and-robberies-2015.db")
cursor = connection.cursor()
cursor.execute("select * from public_assaults_and_robberies_2015")
cursor.fetchall()

# ******This made it easy for me to see the different regions
regions = []
# ***********************************************************
area_outside = []
auckland = []
bay_of_plenty = []
canterbury = []
gisborne = []
hawkes_bay = []
manawatu = []
marlborough = []
nelson = []
northland = []
otago = []
southland = []
taranaki = []
tasman = []
waikato = []
wellington = []
west_coast = []

# Code for my convenience
for row in cursor.execute("select Region_2013_label from public_assaults_and_robberies_2015"):
    regions.append(row[0])
reg = [*set(regions)]
reg.sort()
print(reg)

# ***********************Getting and adding up all of the victim numbers for each Region******************
for row in cursor.execute("select Victimisations_calendar_year_2015 from "
                          "public_assaults_and_robberies_2015 where Region_2013_label = 'Area Outside Region'"):
    area_outside.append(row[0])
ao = sum(area_outside)
print(ao)

for row in cursor.execute("select Victimisations_calendar_year_2015 from "
                          "public_assaults_and_robberies_2015 where Region_2013_label = 'Auckland Region'"):
    auckland.append(row[0])
auck = sum(auckland)
print(auck)

for row in cursor.execute("select Victimisations_calendar_year_2015 from "
                          "public_assaults_and_robberies_2015 where Region_2013_label = 'Bay of Plenty Region'"):
    bay_of_plenty.append(row[0])
bop = sum(bay_of_plenty)
print(bop)

for row in cursor.execute("select Victimisations_calendar_year_2015 from "
                          "public_assaults_and_robberies_2015 where Region_2013_label = 'Canterbury Region'"):
    canterbury.append(row[0])
cant = sum(canterbury)
print(cant)

for row in cursor.execute("select Victimisations_calendar_year_2015 from "
                          "public_assaults_and_robberies_2015 where Region_2013_label = 'Gisborne Region'"):
    gisborne.append(row[0])
gis = sum(gisborne)
print(gis)

for row in cursor.execute('select Victimisations_calendar_year_2015 from '
                          'public_assaults_and_robberies_2015 where Region_2013_label = "Hawke\'s Bay Region"'):
    hawkes_bay.append(row[0])
hb = sum(hawkes_bay)
print(hb)

for row in cursor.execute("select Victimisations_calendar_year_2015 from "
                          "public_assaults_and_robberies_2015 where Region_2013_label = 'Manawatu-Wanganui Region'"):
    manawatu.append(row[0])
man = sum(manawatu)
print(man)

for row in cursor.execute("select Victimisations_calendar_year_2015 from "
                          "public_assaults_and_robberies_2015 where Region_2013_label = 'Marlborough Region'"):
    marlborough.append(row[0])
marl = sum(marlborough)
print(marl)

for row in cursor.execute("select Victimisations_calendar_year_2015 from "
                          "public_assaults_and_robberies_2015 where Region_2013_label = 'Nelson Region'"):
    nelson.append(row[0])
nel = sum(nelson)
print(nel)

for row in cursor.execute("select Victimisations_calendar_year_2015 from "
                          "public_assaults_and_robberies_2015 where Region_2013_label = 'Northland Region'"):
    northland.append(row[0])
north = sum(northland)
print(north)

for row in cursor.execute("select Victimisations_calendar_year_2015 from "
                          "public_assaults_and_robberies_2015 where Region_2013_label = 'Otago Region'"):
    otago.append(row[0])
ota = sum(otago)
print(ota)

for row in cursor.execute("select Victimisations_calendar_year_2015 from "
                          "public_assaults_and_robberies_2015 where Region_2013_label = 'Southland Region'"):
    southland.append(row[0])
south = sum(southland)
print(south)

for row in cursor.execute("select Victimisations_calendar_year_2015 from "
                          "public_assaults_and_robberies_2015 where Region_2013_label = 'Taranaki Region'"):
    taranaki.append(row[0])
tar = sum(taranaki)
print(tar)

for row in cursor.execute("select Victimisations_calendar_year_2015 from "
                          "public_assaults_and_robberies_2015 where Region_2013_label = 'Tasman Region'"):
    tasman.append(row[0])
tas = sum(tasman)
print(tas)

for row in cursor.execute("select Victimisations_calendar_year_2015 from "
                          "public_assaults_and_robberies_2015 where Region_2013_label = 'Waikato Region'"):
    waikato.append(row[0])
wai = sum(waikato)
print(wai)

for row in cursor.execute("select Victimisations_calendar_year_2015 from "
                          "public_assaults_and_robberies_2015 where Region_2013_label = 'Wellington Region'"):
    wellington.append(row[0])
well = sum(wellington)
print(well)

for row in cursor.execute("select Victimisations_calendar_year_2015 from "
                          "public_assaults_and_robberies_2015 where Region_2013_label = 'West Coast Region'"):
    west_coast.append(row[0])
west = sum(west_coast)
print(west)

# ************************Setting up the pie chart and saving it to pdf***********************************
explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05)

graph = pd.DataFrame.from_dict({"Area Outside Region": [ao], "Auckland Region": [auck], "Bay of Plenty Region": [bop],
                                "Canterbury Region": [cant], "Gisborne Region": [gis], "Hawke's Bay Region": [hb],
                                "Manawatu-Wanganui Region": [man], "Marlborough Region": [marl], "Nelson Region": [nel],
                                "Northland Region": [north], "Otago Region": [ota], "Southland Region": [south],
                                "Tasman Region": [tas], "Waikato Region": [wai], "Wellington": [well],
                                "West Coast Region": [west]})

graph_plot = graph.sum().plot(kind="pie", grid=False, title="New Zealand: Assault & Robbery per Region 2015", ylabel="",
                              autopct='%1.0f%%', startangle=60, explode=explode, fontsize=5, figsize=(8, 6)).get_figure()
graph_plot.savefig("victims_population.pdf")