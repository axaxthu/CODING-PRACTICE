#set store multiple values in single variable
#unordered
#unchangable
#non homogenous
#duplicates not allowed (same item cnnot repeat inside a set)
myset={"car","boat","train","bike","tractor"} 
print(myset) #output is not in order
myset.pop() #one is randomly popped
print(myset)

if "boat" in myset:
    print("boat")
else:
    print("sad")    