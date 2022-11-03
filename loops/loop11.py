# w.a.p to display only those numbers from a list that satisfy following condition
#number must be divisible by 5
#if the number is greater than 150 , then skip it and move to the next number
#if the number is greater than 500, stop the loop

numbers= [12,75,150,180,145]

for i in numbers:
    if i<150:
        if i%5==0:
            print(i)
        else:
            continue    
    elif i>150 and i<500:
        continue
    else:
        break 