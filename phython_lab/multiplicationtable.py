n=int(input("Enter the number for multiplication table:"))
limit=int(input("Enter the limit for the multiplication table:"))
for i in range(1,limit+1):
    print(n,"x",i,"=",n*i)
    