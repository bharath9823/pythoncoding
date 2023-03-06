#python program to print a string in reverse if a number of letters in a string are even,
c='My name is king'
l=['i','e','o','u','a','A','E','I','O','U']
d=0
for i in c:
    if i in l:
        d+=1
print(d)
if d%2==0:
    print(c[::-1])
else:
    print(c)