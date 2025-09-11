ss=input("enter a word")
if len(ss)>0:
    f=ss[0]
    h=f+ss[1:].replace(f,'$')
    print(h)