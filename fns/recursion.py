#print factorial of a number using recursion

def fact(n):
    if n==0: # 0! is 1
        return 1
    return n*fact(n-1)    

num=fact(5)
print("FACTORIAL:",num)   
