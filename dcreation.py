#create schema/database and table
import mysql.connector as m
#creating connection object
con_obj=m.connect(user='root',password='root',host='localhost')
print(con_obj)
#creating cursor object
cur_obj=con_obj.cursor()
#creating a table and columns
cur_obj.execute("create table py4.students(id int(10),name varchar(20),course varchar(10),mbno int(10))")
print(cur_obj)
