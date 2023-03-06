#example1
s=input("enter string:")
match s:
    case "a":
        print("a is vowel")
    case "i":
        print("i is vowel")
    case "e":
        print("e is vowel")
    case "o":
        print("o is vowel")
    case "u":
        print("u is vowel")
    case "A":
        print("a is vowel")
    case "E":
        print("i is vowel")
    case "I":
        print("e is vowel")
    case "O":
        print("o is vowel")
    case "U":
        print("u is vowel")
    case _:
        print("the letter is consonent")

#example2
s=input("enter name:")
match s:
    case "bharath":
        print("hey i am bharath how can i help you today?")
    case "Naveen":
        print("hey i am naveen, i have a few questions on life Can you help me with those ?")
    case "Vineeth":
        print("Hey i am Vineeth, Hope you are having a good day!")
    case _:
        print("Hey I am AI, Can't help and won't help you right now!")
#example3
s=input("Enter the Operation that you want to perform:")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
match s:
    case "add":
        print(a+b)
    case "multiply":
        print(a*b)
    case "subtract":
        print(a-b)
    case "divide":
        if(b==0):
            print("can't perform division on Zero denominator, please change value for b:")
            b=int(input("Enter the value for b:"))
            print(round(a/b))
    case _:
        print("Do you still need time to decide on the operation that you want to perform ?")
        _yesOrNo=input("Do you want to proceed with the operation ?")
        if(_yesOrNo=="yes" or _yesOrNo=="Y"):
            s1=input("Enter the Operation that you want to perform:")
            match s1:
                case "add":
                    print(a+b)
                case "multiply":
                    print(a*b)
                case "subtract":
                    print(a-b)
                case "divide":
                    if(b==0):
                        print("can't perform division on Zero denominator, please change value for b:")
                        b=int(input("Enter the value for b:"))
                        print(a/b)
                    else:
                        print(a/b)    
        else:
            print("bye bye!!!")


