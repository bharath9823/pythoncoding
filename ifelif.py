per=int(input("enter Marks:"))
if per>=80 and per<=100:
    print("student got distinction")
elif per>=70 and per<=79:
    print("student got first class")
elif per>=60 and per<=69:
    print("student got second class")
elif per>=50 and per<=59:
    print("student got third class")
elif per>=35 and per<=49:
    print("student got fourth class")
elif per<=34 and per>=0:
    print("student failed")
elif per>100 or per<0:
    print("invalid input")
#elif per<0:
    print("invalid input")
else:
    print("end")