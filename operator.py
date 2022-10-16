#ENTER TWO NUMBERS AND AN OPERATOR
a=int(input("ENTER FIRST NUMBER: "))
b=int(input("ENTER SECOND NUMBER: "))
op=str(input("ENTER AN OPERATOR: "))
#DO CALCULATION ON A AND ACCORDING TO THE OPERATOR
if(op=="+"):
    print(a+b)
elif op=="-":
    print(a-b) 
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
elif op=="%":
    print(a%b) 
elif op=="//":
    print(a//b)
else :
    print("ERROR")                    