#counting a numbers in a list and print highest number
l1=[70,10,20,10,20,30,40,20,30,10,50,60,40,30,10,20,70,70,70]
count={ }
for i in l1:
    if i not in count:
        count[i]=1
    else:
       count[i]+=1
print(count)
print(max(count))

#o/p:{70: 4, 10: 4, 20: 4, 30: 3, 40: 2, 50: 1, 60: 1}
    #70

#counting a numers in a list
l1=[10,70,10,20,10,20,30,40,20,30,10,50,60,40,30,10,20,70,70,70]
def list_count(e):
    c=0
    for i in  l1:
        if i==e:
            c+=1
    return c
d1={}
for i in set(l1):
    d1.update({i:list_count(i)})
print(d1)
#o/p:{70: 4, 10: 4, 20: 4, 30: 3, 40: 2, 50: 1, 60: 1}