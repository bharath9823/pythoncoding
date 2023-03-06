#1
n=int(input())
val=ord("A")
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print(chr(val),end=" ")
        else:
            print(" ",end=" ")
        val+=1
        if val>ord("Z"):
            val=ord("A")
    print()
#o/p:5
# A B C D E 
# F       J
# K       O
# P       T
# U V W X Y
#2
n=int(input("n:"))
val=ord("Z")
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print(chr(val),end=" ")
        else:
            print(" ",end=" ")
        val-=1
        if val<ord("A"):
            val=ord("Z")
    print()
    #o/p:5
# Z Y X W V 
# U       Q 
# P       L 
# K       G 
# F E D C B 
#3
n=int(input("n:"))
for j in range(n):
    for i in range(n):
        if i==0:
            print("*",end=" ")
        elif j==0:
            print("#",end=" ")
        elif i==n-1:
            print("@",end=" ")
        elif j==n-1:
            print("$",end=" ")
        else:
            print(" ",end=" ")
    print()
#o/p:5
# * # # # # 
# *       @ 
# *       @ 
# *       @ 
# * $ $ $ @