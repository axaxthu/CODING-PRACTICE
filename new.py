
emp= str(input("ENTER EMPLOYEE NAME: "))
sal= float(input("ENTER YOUR SALARY: "))
yos= int(input("ENTER YEARS OF SERVICE: "))

if(yos>5):
    sal+=1000
    print("net bonus amount: ",sal)
else:
    print("net bonus amount: ", sal)