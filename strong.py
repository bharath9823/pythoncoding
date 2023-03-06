#finding strong number using recursion
def fact(n):
    if n==1:
        return 1
    return fact(n-1)*n

def strong(a,s=0):
    if a==0:
        return s
    strong(a//10,s+fact(a%10))
print(strong(145))