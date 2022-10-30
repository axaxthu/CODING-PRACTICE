name=str(input("ENTER YOUR NAME: "))

print(name[0])
print(name[-1])

if len(name)%2==0:
    mid=(len(name)/2)
    print(name[int(mid)])
else:
    mid=(int((len(name))/2))+1
    print(name[int(mid)-1])
