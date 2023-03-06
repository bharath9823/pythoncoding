'''l1=[10,20,30,100,11.1,120]
for i in l1:
    print(i,end=" ")
print()
for i in range(len(l1)):
    print(i,end=" ")'''
#copy
'''l1=[10,30,50,20,90,67]
l2=l1.copy()
print(l2)'''
#clear
'''l3=[10,20,40]
print(l3.clear())'''
#append
'''l2.append([66,77,88,44,55])
print(l1)
print(l2)'''
#extend
'''l1=[44,585,85,23,848,54]
l1.extend('thor')
print(l1)
l1.extend([100,2300,556,66677,8,778,8,8,86,8688,8,])
print(l1)'''
#pop
'''l1=[10,20,30,40,50,9,0,8,0,522]
print(l1.pop())
print(l1)'''
#remove
'''l1=[10,20,30,40,50,90,80,522]
l1.remove(10)
print(l1)'''
#sort
'''l1=[10,20,30,40,50,90,80,522]
l1.sort()
print(l1)'''
#index
'''l1=[10,20,30,40,50,90,10,80,522]
l2=l1.index(10,1)#value and index num where to start
print(l2)'''
#count
'''l1=[10,20,30,40,50,90,10,80,522,30,40,50]
print(l1.count(50))
print(l1)'''
#insert
'''l1=[10,20,30,40,50]
l1.insert(0,'naveen')#(index, and insertion value)
print(l1)
l1.insert(1,'pooja')
print(l1)'''
#reverse using sort
'''l1=[10,20,30,40,50,90,10,80,522,30,40,50]
l1.sort(reverse=True)
print(l1)'''
#deep copy
'''t1=[10,20,30,45,60]
t2=t1
t2.extend([30,50,70,880])
print(t1)
print(t2)'''
#shallow copy
'''t1=[10,40,60]
t2=t1.copy()
t2.extend([80])
print(t1)
print(t2)'''
#tuple index,count
'''t1=(10,30,50,70,10,30)
print(t1.index(10))
print(t1.count(10))'''
#l1=[val for val in range(1,11,1) if val%2==0 val%3==0]
#print(l1)
'''l1=[]
for x in range(1,4):
    for y in range(1,4):
        l1.append(x)
print(l1)'''#[1, 1, 1, 2, 2, 2, 3, 3, 3]
'''l1=[y for x in range(1,4) for y in range(1,4)]
print(l1)'''#[1, 2, 3, 1, 2, 3, 1, 2, 3]
#adding elements into a tuple using list
'''t1=(10,30,40,60,70)
t2=list(t1)#type casting
t2.extend([100,200])
print(t1)
t1=tuple(t2)
print(t1)'''
#sets,add,remove
'''s1={10,20,30,50,90,80}
s1.add(300)
print(s1)
s1.remove(300)
print(s1)
s1.remove(10)
print(s1)'''
#discard
'''s1={10,30,50,70}
s1.discard(300)#it does not throw error
print(s1)'''
#clear
'''s1={10,20,30,60,80,90}
s1.clear()
print(s1)'''#return empty set
#copy
'''s1={10,20,30,60,80,90}
s2=s1.copy()
print(s2)
s1.add(40)
print(s1)'''
'''s1={10,20,30,60,80,90}
print(s1)
s1.pop()
print(s1)'''


'''s1={10,20,30,40,50,60}
s2={100,200,10,300,400,40}
s3={1000,2000,100,10,50,3000,4000,300}
print(s1)
print(s1.union(s2))#{100, 40, 200, 10, 300, 400, 50, 20, 60, 30}
print(s1.union(s3))#{4000, 100, 40, 1000, 10, 300, 2000, 50, 20, 3000, 60, 30}
print(s1.intersection(s2))#{40, 10}
print(s1.intersection(s3))#{50, 10}
print(s1.intersection_update(s2))
print(s1)#{40, 10}
print(s1.difference(s2))#print s1 unique values ,common elemnets are negletted {50, 20, 60, 30}
print(s1.difference(s3))#{40, 20, 60, 30}
s1.difference_update(s2)
print(s1)#{50, 20, 40, 10, 60, 30}
        {50, 20, 60, 30}
print(s1.symmetric_difference(s2))#eliminate all common elemnts from both the sets.
s1.symmetric_difference_update(s2)
print(s1)#eleminate the common eliments from bothe the sets and update it to the s1.
#superset,subset,isdisjoint these built in methods give boolean output
set_1={10,20,30,40,50}
set_2={40,50}
set_3={50,70,809,90}
print(set_1.issuperset(set_2))#True
print(set_1.issubset(set_2))#false
print(set_2.issuperset(set_1))#false
print(set_2.issubset(set_1))#true
print(set_1.isdisjoint(set_2))#false'''












