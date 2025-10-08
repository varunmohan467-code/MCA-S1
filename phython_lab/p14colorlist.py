list1= input("Enter colors in list 1(seperated with spece):").split()
list2= input("Enter colors in list 2(seperated with spece):").split()
result=[]
for color in list1:
    if color not in list2:
        result.append(color)
        print(result)