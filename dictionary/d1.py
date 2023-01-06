mydic={
    "name":'Ananthu',
    "age":21,
    "CGPA":8.5
}

print(mydic.get("name")) #access value in name
print(mydic.keys()) #access keys
print(mydic.items())
mydic["name"]="DHAADHA" #updation method 1
print(mydic)
mydic.update({"age":25}) #updation mthod 2
print(mydic)
mydic.pop("age")

print(mydic)
