#INPUT THREE SIDES AND CHECK WHETHER IT IS POSSIBLE TO FORM A TRIANGLE WITH IT
a=int(input("ENTER SIDE 1: "))
b=int(input("ENTER SIDE 2: "))
c=int(input("ENTER SIDE 3: "))

if a+b>c:
    print("it is possible to form a traingle")
else:
    print("it is not possible to form a triangle")    

