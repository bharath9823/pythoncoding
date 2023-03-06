
#python program to print if addition and product  of input number is even 
#print it reverse else print it as it is(without using loops anfd built in fun's)
n=503
c=((n//10)%10)+n//100+n%10
e=((n//10)%10)*n//100*n%10
print(c+e)
f=c+e

d=str(n)
if f%2==0:
    print(d[::-1])
else:
    print(n)
