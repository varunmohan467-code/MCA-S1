strr=input("Enter a string")
if strr.endswith("ing"):
    strr=strr+"ly"
else:
    strr=strr+"ing"
    print("Modified string:",strr)