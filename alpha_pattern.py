# def fun(n):
#     val=ord("A")
#     for i in range(n):#(1,n+1)
#         for j in range(n):
#             if i+j>=n-1:
#                  print(chr(val),end=" ")
#                  val-=1
#             else:print(" ",end=" ")
#         print()
#         val+=(i+1)*2+1  #(1*2+1)
# fun(5)
#         A 
#       C B 
#     F E D
#   J I H G
# O N M L K
# def fun(n):
#     val=ord("A")
#     for i in range(n):#(1,n+1)
#         for j in range(n):
#             if i+j>=n-1:
#                  print(chr(val),end=" ")
#                  val-=1
#                  if val<ord("A"):
#                     val=ord("Z")
#             else:print(" ",end=" ")
#         print()
#         val+=(i+1)*2+1
#         while val>ord("Z"):
#             val-=26
# fun(int(input()))
#                   A 
#                 C B 
#               F E D 
#             J I H G 
#           O N M L K 
#         U T S R Q P 
#       B A Z Y X W V 
#     J I H G F E D C 
#   S R Q P O N M L K 
# C B A Z Y X W V U T 





def fun(n):
    val=ord("A")
    for i in range(n):
        for j in range(n):
            if i+j>=n-1:
                 print(chr(val),end=" ")
                 val-=1
                 if i+j==4:
                    print(chr(val),end=" ")
            else:print(" ",end=" ")
        print()
        while val>ord("Z"):
             val-=26       
fun(5)
# def fun(n):
#     for i in range(n):
#         val=ord("U")+i%26
#         for j in range(n):
#                  print(chr(val),end=" ")
#                  val-=n
#         while val>ord("A"):
#             val-=26
#         print()
            
# fun(5)
# U P K F A
# V Q L G B
# W R M H C
# X S N I D
# Y T O J E