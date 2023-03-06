n=int(input("Enter number of rows: "))
a=1
for i in range(n+1):
    for space in range(n-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            a = 1
        else:
            a = a* (i - j)//j
        print(a, end = " ")
    print()
#      1 
#     1 1 
#    1 2 1 
#   1 3 3 1
#  1 4 6 4 1