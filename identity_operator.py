#ex1
a=40
print(id(a))
a1=50-10
print(id(a1))
a2=10+10+10+10+20-20
print(id(a2))
#ex2
a="ir"
b="shan"
c="irshan"
d=a+b
print(d)
print(c)
print(a is b)
print(d is c)
print(b is not c)
print(c is d)
print(id(c),id(d))
#ex3
a=20+20
h=40
b=20
print(h is a)
print(a is b)
#ex4
e='irshan'
c='ir'+'shan'
print(c)
print(e is c)
print(id(e),id(c))
print(id(a),id(h))


