# Import SQL Module For Database Connection
import mysql.connector as mysql

# Open Database Connection
db = mysql.connect(host="localhost", user="root",
                   password="", database="stud")

# Create cursor object using cursor method
cursor = db.cursor()

# SQL Query
sql = "SELECT * FROM bca"

# Execute cursor method
cursor.execute(sql)

# Get data from the database
data = cursor.fetchall()
for i in data:
    print(i)

# Close Database Connection
db.close()
