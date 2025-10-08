nums=list(map(int,input("Enter a list pof integers seperated by spaces:").split()))
result=[]
for n in nums:
    if n%2!=0:
        result.append(n)
        print("Entered Number:",nums)
        print("List after removing even numbers:", result)