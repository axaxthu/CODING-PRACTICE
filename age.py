age1= int(input("enter age 1: "))
age2= int(input("enter age 2: "))
age3= int(input("enter age 3: "))

if age1>age2:
    if age2>age3:
     print("youngest is: ", age3)
     print("oldest is: ", age1)
    elif age1>age3:
       print("youngest is: ", age2)
       print("oldest is: ", age1)
    else:
        print("oldest is ", age3)
        print("youngest is: ", age2)   

elif age2>age1:

     if age1>age3:
       print("youngst is: ",age3)
       print("oldest is: ", age2)
     elif age2>age3:
        print("youngst is: ",age1)
        print("oldest is: ", age2)
     else: 
          print("oldest is ", age3)
          print("youngst is: ",age1)    
elif age2==age1==age3:
    print("age are same") 



