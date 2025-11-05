word=input("Enter a line of text:").split(' ')
c={}
for t in word:
     if t in c:
        c[t]+=1
     else:
        c[t]=1
        print(c)