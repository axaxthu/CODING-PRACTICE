#ASSIGN GRADES ACCORDING TO MARK


marks= int(input("ENTER YOUR MARK: "))

if marks<=100 and marks>90:
    print("YOUR GRADE IS A")
elif marks<=90 and marks>80:
    print("YOUR GRADE IS B")
elif marks<=80 and marks>70:
    print("YOUR GRADE IS C")
elif marks<=70 and marks>=0:
    print("YOUR GRADE IS D")
elif marks<100:
    print("nvalid")
    
