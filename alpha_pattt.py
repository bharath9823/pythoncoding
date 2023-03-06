#1
n=int(input("n:"))                      
val=ord("A")
for i in range(n):
    for j in range(n):
        print(chr(val),end=" ")
        val+=1
    print()
#A B C D E 
#F G H I J
#K L M N O
#P Q R S T
#U V W X Y


#2
n=int(input("n:"))                      
val=ord("A")
for i in range(n):
    for j in range(n):
        print(chr(val),end=" ")
        val+=1
        if val>ord("Z"):
            val=ord("A")
    print()
# o/p:
# n:10
# A B C D E F G H I J 
# K L M N O P Q R S T 
# U V W X Y Z A B C D 
# E F G H I J K L M N 
# O P Q R S T U V W X 
# Y Z A B C D E F G H 
# I J K L M N O P Q R 
# S T U V W X Y Z A B 
# C D E F G H I J K L 
# M N O P Q R S T U V 

#3
n=int(input("n:"))                      
val=ord("A")
for i in range(n):
    for j in range(n):
        print(chr(val),end=" ")
        val+=1
        if val>ord("Z"):
            val=ord("A")
        print()
#o/p:
# n:5
# A 
# B 
# C 
# D 
# E 
# F 
# G 
# H 
# I
# J
# K
# L
# M
# N
# O
# P
# Q
# R
# S
# T
# U
# V
# W
# X
# Y


#4
n=int(input("n:"))                      
val=ord("A")
for i in range(n):
    for j in range(n):
        print(chr(val),end=" ")
    val+=1
    if val>ord("Z"):
        val=ord("A")
    print()
#o/p:5
#A A A A A 
#B B B B B
#C C C C C
#D D D D D
#E E E E E
#different ways for 4th program
#1
for i in 'ABCDE':
    for j in 'ABCDE':
        print(i,end=" ")
    print()
#2
for i in range(65,70):
    for j in range(65,70):
        print(chr(i),end=" ")
    print()
#3
n=int(input())
val=ord("A")
for i in range(n):
    print(f"{chr(val)} "*n)
    val+=1
#5
n=int(input())
for i in range(n):
    val=ord("A")
    for j in range(n):
        print(chr(val+j),end=" ")
    val+=1
    if val>ord("Z"):
        val=ord("A")
    print()
#o/p
#A B C D E 
#A B C D E 
#A B C D E 
#A B C D E 
#A B C D E
'''n=int(input())
val=ord("A")
for i in range(n):
    for j in range(n):
        print(chr(val+j),end=" ")
    print()'''
#6
n=int(input())
val=ord("Z")
for i in range (n):
    for j in range(n):
        print(chr(val),end=" ")
        val-=1
    if val<ord("A"):
        val=ord("Z")
    print()
#o/p:
#5
#Z Y X W V
#U T S R Q
#P O N M L
#K J I H G
#F E D C B

#7
n=int(input("n:"))
val=ord("E")
for i in range(n):
    for j in range(n):
        print(chr(val),end=" ")
        val+=1
        if val>ord("Z"):
            val=ord("A")
    print()
#o/p:
# n:5
# E F G H I 
# J K L M N 
# O P Q R S 
# T U V W X 
# Y Z A B C 

#8
for i in range(1,6):
    for j in range(5,0,-1):
        if i<=j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
#o/p:
# * * * * *
# * * * *
# * * *
# * *
# *

#9
for i in range(1,6):
    for j in range(5,0,-1):
        if i>=j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
#o/p:
#     *
#    **
#   ***
#  ****
# *****
