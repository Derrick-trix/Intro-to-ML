a = input("Give a list of numbers separated by space:")
numbers=a.split(" ")
b=[]
i=0
while(i<len(numbers)):
    b.append(int(numbers[i]))
    i+=1
c=b.sort()
print("Given numbers sorted:",b)



