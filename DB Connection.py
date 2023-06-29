# Import SQL Module For Database Connection
import mysql.connector as mysql

# Open Database Connection
db = mysql.connect(host="localhost", user="root",
                   password="", database="stud")

# Create cursor object using cursor method
cursor = db.cursor()

# SQL Query
cursor.execute("SELECT VERSION()")

data = cursor.fetchone()
print("Database Version: ", data)

# Close Database Connection
db.close()
