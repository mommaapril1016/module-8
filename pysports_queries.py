import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="VanHaitsma1016",
    database="pysports"
)

# Create a cursor
cursor = db.cursor()

# Write the query
query = "SELECT team_id, team_name, mascot FROM team"

# Execute the query
cursor.execute(query)

# Iterate over the cursor
for team in cursor:
    print(team)

# Close the cursor
cursor.close()

# Close the database
db.close()

Team Table

 

SELECT team_id, team_name, mascot

FROM team;

Explanation:

Player table

SELECT player_id, player_name, team_id

FROM player;

The SELECT statement is used to select data from a database table.

Select syntax

SELECT column1, column2, ...
FROM table_name;

 

To select everything from a given table, use the following command.

SELECT * FROM table_name;
