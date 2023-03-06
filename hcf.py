#hcf or lcm program using the recursion function
def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)
print(hcf(15,27))
#print(obj)
#Method 2 using the recursion
a=int(input("a:"))
b=int(input("b:"))
def fun(n):
    if a%n==0 and b%n==0:
        return n
    else:
        return fun(n-1)
print(fun(a))