salary= float(input("ENTER EMPLOYEE SALARY: "))
timesp= int(input("ENTER TIME SPEND IN THE COMPANY(IN YEARS); "))

if(timesp>10):
    nb= salary + .10*salary
    print("EMPLOYEE NET SALARY: " ,nb)
elif(timesp<=10 and timesp>6 ):
    nb= salary + .08*salary
    print("EMPLOYEE NET SALARY: " ,nb)
elif(timesp<6):
    nb= salary + .05*salary
    print("EMPLOYEE NET SALARY: " ,nb)      