import os
import pymysql

#Get username form the clou9 workspace
#(Modify this if you were running on another evironment)

username = os.getenv("$C9_USER")

#Connecting to the database

connection = pymysql.connect(host='localhost', 
                            user=username, 
                            password='', 
                            db='Chinook')

try:
    #Run a query against the database
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #Close the connection to SQL, regardless of whether the above was successful. 
    connection.close()
    
    