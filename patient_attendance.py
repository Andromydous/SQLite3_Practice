import sqlite3
import pandas as pd
import matplotlib

connection = sqlite3.connect("patients.db")
cursor = connection.cursor()
cursor.execute("select * from patient_attendance")
cursor.fetchall()

male_follow_up_above_50_yes = []
male_follow_up_above_50_no = []
male_follow_up_below_50_yes = []
male_follow_up_below_50_no = []
female_follow_up_above_50_yes = []
female_follow_up_above_50_no = []
female_follow_up_below_50_yes = []
female_follow_up_below_50_no = []

for row in cursor.execute("select patient_id from patient_attendance where gender = 'M' and age < 50 "
                          "and follow_up_attended == 'Yes'"):
    male_follow_up_below_50_yes.append(row)

for row in cursor.execute("select patient_id from patient_attendance where gender = 'F' and age < 50 "
                          "and follow_up_attended == 'Yes'"):
    female_follow_up_below_50_yes.append(row)

for row in cursor.execute("select patient_id from patient_attendance where gender = 'M' and age < 50 "
                          "and follow_up_attended == 'No'"):
    male_follow_up_below_50_no.append(row)

for row in cursor.execute("select patient_id from patient_attendance where gender = 'F' and age < 50 "
                          "and follow_up_attended == 'No'"):
    female_follow_up_below_50_no.append(row)

for row in cursor.execute("select patient_id from patient_attendance where gender = 'M' and age >= 50 "
                          "and follow_up_attended == 'Yes' "):
    male_follow_up_above_50_yes.append(row)

for row in cursor.execute("select patient_id from patient_attendance where gender = 'F' and age >= 50 "
                          "and follow_up_attended == 'Yes' "):
    female_follow_up_above_50_yes.append(row)

for row in cursor.execute("select patient_id from patient_attendance where gender = 'M' and age >= 50 "
                          "and follow_up_attended == 'No' "):
    male_follow_up_above_50_no.append(row)

for row in cursor.execute("select patient_id from patient_attendance where gender = 'F' and age >= 50 "
                          "and follow_up_attended == 'No' "):
    female_follow_up_above_50_no.append(row)

x = {"Male: Follow-up below 50": [len(male_follow_up_below_50_yes)],
     "Male: No Follow-up below 50": [len(male_follow_up_below_50_no)],
     "Female: Follow-up below 50": [len(female_follow_up_below_50_yes)],
     "Female: No Follow_up below 50": [len(female_follow_up_below_50_no)],
     "Male: Follow-up above 50": [len(male_follow_up_above_50_yes)],
     "Male: No Follow-up above 50": [len(male_follow_up_above_50_no)],
     "Female: Follow-up above 50": [len(female_follow_up_above_50_yes)],
     "Female: No Follow-up above 50": [len(female_follow_up_above_50_no)]}


graph = pd.DataFrame.from_dict(x)

graph_plot = graph.plot(kind="bar", grid=True, title="Patient Attendance", ylabel="Follow-up Count",
                        xlabel="Patients", width=3, linewidth=10, ylim=(0, 50)).get_figure()
graph_plot.savefig("patient_follow_up.pdf")