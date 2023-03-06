import mysql.connector as m
#con_obj=None
#try:

con_obj=m.connect(user='root',password='root',host='localhost')
print(con_obj)
cur_obj=con_obj.cursor()
cur_obj.execute("insert into py4.students(id,name,course,mbno)values(101,'Bharath','Python FL',998691838)")
print(cur_obj)
#except:
#print("check your given credentials")