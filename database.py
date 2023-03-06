#creating cursor object and connection object using exception handling
import mysql.connector as m
con_obj=None
try:
    con_obj=m.connect(user='root',password='root',host='localhost')
    print(con_obj)
    cur_obj=con_obj.cursor()
    cur_obj.execute("show databases")
    for i in cur_obj:
        print(i)
except:
    print("errors occured check ur credentials")
