#TO FIND AREA OF A TRIANGLE
b= int(input("enter length of the triangle: "))
h= int(input("enter height of the triangle: "))

area= 0.5*b*h

print("AREA OF THE TRIANGLE USING BH FORMULA: ",area)

#ANOTHER METHOD TO FIND AREA
a=int(input("enter side 1: "))
b= int(input("enter side 2: "))
c= int(input("enter side 3: "))
 
s=(a+b+c)/2
 
area2= (s*(s-a)*(s-b)*(s-c))**0.5

print("AREA OF THE TRIANGLE USING HERON'S FORMULA IS :", area2)