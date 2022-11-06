#printing as arguments

def name(*args): #this is used when you don't knpw the number of arguments you might be using 
    print(args)  #OUTPUT WILL BE ("ANANTHU","IS","OP") 
    print(args[0]) #element in the specific index will only be printed

name("ANANTHU","IS","OP")