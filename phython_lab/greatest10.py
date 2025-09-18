n1=int(input("Enter first Number::"))
n2=int(input('Enter second NUmber::'))
n3=int(input("Enter second number::"))
if n1>= n2 and n1 >= n3:
    largest = n1
elif n2>=n1 and n2>=n3:
    largest = n2
else :
    largest = n3


print("The Largest of All 3 Numbers is ::",largest)