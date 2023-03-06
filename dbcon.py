#importing the mysql connector or external package
import mysql.connector as m
#establish the connection by creating the connection object
con_obj=m.connect(user="root",password="root",host="localhost")
print(con_obj)
#creating the curser object to execute the queries
cur_obj=con_obj.curser()
print(cur_obj)
#displaying the database Names
con_obj.execute("show databases")

