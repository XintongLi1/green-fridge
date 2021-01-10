import mysql.connector as mc

# Open database connection
db = mc.connect(host="localhost", user="root", passwd="root")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Database version : %s " % data)


# execute SQL query using execute() method.
cursor.execute("DROP TABLE IF EXISTS USER_ACCOUNT")

sql = """
        CREATE TABLE USER_ACCOUNT(
         USER_NAME CHAR(20) NOT NULL, 
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         PASSWORD INT,
         )
         """
cursor.execute(sql)

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
#print "Database version : %s " % data

# disconnect from server
db.close()