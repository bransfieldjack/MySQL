import os
import pymysql

#Get username from the clou9 workspace
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
        cursor.execute("DELETE FROM Friends WHERE name = %s;", ['bob', 'jim'])
        connection.commit()
finally:
    #Close the connection to SQL, regardless of whether the above was successful. 
    connection.close()
    
    