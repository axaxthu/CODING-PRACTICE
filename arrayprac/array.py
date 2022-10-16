a="HELLO WORLD"
#printing a particular index
print(a[7])
#printing the length of a
print(len(a))


x="ananthu","namit","puru"
#printing a particular index
print(x[1])
#printing the length of x
print(len(x))

y= "ananthapadmanabhan is a genius man and this could be a rumour"
#checking whether a word is present
if "genius" in y:
    print("YES! its there")
else:
    print("no")    

#replacing a word present
if "man" in y:
    print(y.replace("man","mastermind"))
else:
    print(y) 

#checking if a number is not there or not
if "rum" not in y: #rum is actually there in "RUMour"
    print("yes")
else :
    print("no")    