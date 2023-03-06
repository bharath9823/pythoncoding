import mysql.connector as m
#con_obj=None
#try:
con_obj=m.connect(user='root',password='root',host='localhost') #database='py4')
print(con_obj)
val=[(12,'Darshini','java',99049384),(13,'Naveen','javas',8894858),(14,'pooja','devops',72094984)]
#query to insert values into the database 
qry="insert into py4.students(id,name,course,mbno) values(%s,%s,%s)"
cur_obj=con_obj.cursor()
cur_obj.executemany(qry,val)
con_obj.commit()
print(cur_obj)