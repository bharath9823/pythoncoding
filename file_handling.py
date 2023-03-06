#read mode in file handling
f=open("p1.txt","r")
print(f)
if f.closed:
    print("the file is closed")
else:
    print("the file is opened")
res=f.read()
print(res)
f.seek(0)
f.close()
if f.closed:
    print("the file is closed")
else:
    print("the file is opened")
#write mode in file handling
f=open("p2.txt","w")
if f.writable():
    print("the file is writable")
else:
    print("the file is not writable")
f.write("Bharath is a good boy\n")
f.close()
f=open("f3.txt","w+")
l1=["bharath\n","Darshini\n","Naveen\n","pooja\n"]
f.writelines(l1)
f.close()
#Append mode in file handling
f=open("p2.txt","a")
l1=["bharath\n","Darshini\n","Naveen\n","pooja\n"]
f.writelines(l1)
f.close()
f=open("p1.txt","a+")
if f.readable():
    print (True)
else:
    print(False)
if f.writable():
    print(True)
else:
    print(False)
print(f.readlines(1))
print(f.read(1))
f.write("Naveen\n")
f.close()