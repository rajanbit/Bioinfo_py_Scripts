# Importing modules
import mysql.connector as mc

# Connecting to local MySQL database
mysql=mc.connect( host="localhost", user="user1", passwd="", database="16srRNAdb")

mycursor = mysql.cursor()
# Select everything from myseq table where 7dd1e0c5450f0ff6c59187d02ae5783b (hash) found
mycursor.execute("SELECT * FROM myseq WHERE seq LIKE '7dd1e0c5450f0ff6c59187d02ae5783b'") 
myresult = mycursor.fetchall()

# Printing column-1 of the result
for x in myresult:
  print(x[0])
  
# Usage: python mysqldb_find.py
