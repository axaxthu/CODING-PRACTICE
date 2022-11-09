#create a function using following conditions
#it should accept employee name and salary and display both
#if the salary is missing in the function then assign the default salary 10000
#ben(9000) mike(15000) bob()

def office(empn,sal=10000):
    print("EMPLOYEE NAME: "+empn)
    print("EMPLOYEE SALARY:",sal)

office("Ben",9000)
office("mike",15000)
office("Bob")
