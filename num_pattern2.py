class pattern:
    def __init__(self,n):
        self.n=n
    def fun(self):
        for i in range(self.n):
            #val=ord("a")+i
            val=1
            for j in range(self.n+i):
                if i+j>=self.n-1:
                    #print(chr(val),end=" ")
                    print(i,end=" ")
                    # if j<self.n-1:
                    #     val+=1
                    # else:val+=1
                    val+=1
                else:print(" ",end=" ")
            print()
obj1=pattern(5)
obj1.fun()
#o/p:
#         0 
#       1 1 1 
#     2 2 2 2 2 
#   3 3 3 3 3 3 3 
# 4 4 4 4 4 4 4 4 4 