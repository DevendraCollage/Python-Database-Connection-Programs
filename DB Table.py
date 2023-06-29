# Import SQL Module For Database Connection
import mysql.connector as mysql

# Open Database Connection
db = mysql.connect(host="localhost", user="root",
                   password="", database="stud")

# Create cursor object using cursor method
cursor = db.cursor()

# SQL Query
sql = """CREATE TABLE bca(
         first_name char(20),
         last_name char(20),
         age int,
         city char(10),
         gender char(1))"""

try:
    # Execute cursor method
    cursor.execute(sql)
    # Commit in the database
    db.commit()
except:
    # Rollback in the database
    db.rollback()

# Close Database Connection
db.close()
