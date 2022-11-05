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
#to print from 2 ranges
print(y[2:8]) #it is printed from index 2 to index 7 
print(y[:7]) #it is printed from index 0 to 6
print(y[:]) #to print from index 0 to index n-1(the whole string is printed)

#ptrint using negative index(starts from -1:which is the last element)
print(a[-5:-2])



