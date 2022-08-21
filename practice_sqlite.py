import sqlite3
import pandas as pd
import matplotlib

connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()
cursor.execute("select * from customers")
cursor.fetchall()

usa_customers = []
north_american_customers = []
european_customers = []
south_and_central_american_customers = []
uk_and_aussie_customers = []
eastern_europe_and_asia_customers = []

# for row in cursor.execute("select FirstName, LastName from customers where Country == 'USA'"):
#     usa_customers.append(row)
#
# for first, last in usa_customers:
#     print(f"{first} {last}")

# for row in cursor.execute("select FirstName, LastName, Email from customers where Country == 'USA' or Country == 'Canada'"):
#     north_american_customers.append(row)
#
# for row in cursor.execute("select FirstName, LastName, Email from customers where Country = 'Argentina' or "
#                           "Country == 'Brazil' or Country == 'Chile' or Country == 'Portugal'"):
#     south_and_central_american_customers.append(row)
#
# for row in cursor.execute("select FirstName, LastName, Email from customers where Country = 'United Kingdom' "
#                           "or Country == 'Ireland' or Country == 'Australia'"):
#     uk_and_aussie_customers.append(row)
#
# for row in cursor.execute("select FirstName, LastName, Email from customers where Country = 'Austria' or "
#                           "Country == 'Belgium' or Country == 'Denmark' or Country == 'Finland' or Country == 'France' "
#                           "or Country == 'Germany' or Country == 'Hungary' or Country == 'Italy' or "
#                           "Country == 'Netherlands' or Country == 'Norway' or Country == 'Poland' or "
#                           "Country == 'Spain' or Country == 'Sweden'"):
#     european_customers.append(row)
#
# for row in cursor.execute(
#         "select FirstName, LastName, Email from customers where Country = 'Czech Republic' or Country == 'India'"):
#     eastern_europe_and_asia_customers.append(row)

for row in cursor.execute("select FirstName from customers where Country == 'USA' or Country == 'Canada'"):
    north_american_customers.append(row)

for row in cursor.execute("select FirstName from customers where Country = 'Argentina' or "
                          "Country == 'Brazil' or Country == 'Chile' or Country == 'Portugal'"):
    south_and_central_american_customers.append(row)

for row in cursor.execute("select FirstName from customers where Country = 'United Kingdom' "
                          "or Country == 'Ireland' or Country == 'Australia'"):
    uk_and_aussie_customers.append(row)

for row in cursor.execute("select FirstName from customers where Country = 'Austria' or "
                          "Country == 'Belgium' or Country == 'Denmark' or Country == 'Finland' or Country == 'France' "
                          "or Country == 'Germany' or Country == 'Hungary' or Country == 'Italy' or "
                          "Country == 'Netherlands' or Country == 'Norway' or Country == 'Poland' or "
                          "Country == 'Spain' or Country == 'Sweden'"):
    european_customers.append(row)

for row in cursor.execute(
        "select FirstName, LastName, Email from customers where Country = 'Czech Republic' or Country == 'India'"):
    eastern_europe_and_asia_customers.append(row)
    
connection.close()

x = {"North America": [len(north_american_customers)], "South/Central America": [len(south_and_central_american_customers)],
     "UK/Australia": [len(uk_and_aussie_customers)], "Western Europe": [len(european_customers)],
     "East Europe/Asia": [len(eastern_europe_and_asia_customers)]}

graph = pd.DataFrame.from_dict(x)
graph.plot(kind="bar", grid=True, title="Customers by Region", ylabel="Customers", xlabel="Regions")

graph_plot = graph.plot(kind="bar", grid=True, title="Customers by Region", ylabel="Customers", xlabel="Regions",
                        width=3, linewidth=10).get_figure()
graph_plot.savefig("my_graph.pdf")

# print("North American Customers")
# print("*******************************")
# for first, last, email in north_american_customers:
#     print(f"{first} {last}: {email}")
# print()
# print("South and Central American Customers")
# print("**************************************")
# for first, last, email in south_and_central_american_customers:
#     print(f"{first} {last}: {email}")
# print()
# print("European Customers")
# print("***********************************")
# for first, last, email in european_customers:
#     print(f"{first} {last}: {email}")
# print()
# print("UK and Aussie Customers")
# print("************************************")
# for first, last, email in uk_and_aussie_customers:
#     print(f"{first} {last}: {email}")
# print()
# print("Eastern Europe and Asia Customers")
# print("*******************************************")
# for first, last, email in eastern_europe_and_asia_customers:
#     print(f"{first} {last}: {email}")
