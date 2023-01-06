#

numbers=[1,2,3,4,5,2,6]

n=numbers.index(2)
numbers.pop(n) #removes the element in that index
numbers.insert(n,200) #adds element
print(numbers)