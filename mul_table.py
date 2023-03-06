
#this is a program to display multiplication table
#example for nested-while loop in Python
i=1
while i<=10:
  j=1
  while j<=10:
        print(i*j,end=" "),
        j+=1
  i+=1
  print ("\n")
#method 2
i=1
while i<=3:
    j=1
    while j<=5:
        print(i,"*",j,"=",i*j)
        j=j+1
    i=i+1
    print()
