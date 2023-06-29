# Import SQL Module For Database Connection
import mysql.connector as mysql

# Open Database Connection
db = mysql.connect(host="localhost", user="root",
                   password="", database="stud")

# Create cursor object using cursor method
cursor = db.cursor()

# SQL Query
sql = """UPDATE bca
         SET city="Ahmadabad"
         WHERE age=20"""

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
