#create a function in such a way that we can pass any number of arguments to this and it should display  each arguments value

def each(*args):
    for i in args:
        print(i)

each(1,2,2,4,5,6,7,9)        