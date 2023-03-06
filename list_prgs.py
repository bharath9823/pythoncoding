#Finding the index of the given list 
l1=[20,89,67,34,56,78,90,12,34,]
print(l1)
a=int(input())
for i in range(len(l1)):
    if l1[i]==a:
        print(f"{a} is present in the {i}")
        break
else:
    print(f"{a} is ont in list")
#coverting single dimension list to multi dimensional list
l1=[20,89,67,34,56,78,90,12,34,]
def convert(l1,k):
    return [l1[i:i+k] for i in range(0,len(l1),k)]
print(convert(l1, 2))
print(convert(l1, 3))
#Method 2
l1=[20,89,67,34,56,78,90,12,34,]
print(l1)
l2=[]
k=int(input())
for i in range(0,len(l1),k):
    l2.append(l1[i:i+k])
print(l2)
#METHOD 3
l1=[[20, 89], [67, 34], [56, 78], [90, 12], [34]]
def convert(l1, k):
    return(l1,len(l1)//k)

print(convert(l1,2))
print(convert(l1,3))
print(convert(l1,4))
