student={"Anu":[85,90,78],"Gowri":[72,88,91],"Vishnu":[95,80,85]}
for name,marks in student.items():
    total=sum(marks)
    average = sum(marks) / len(marks)
    print(f"Student:{name}")
    print(f"marks:{marks}")
    print(f"Total Marks:{total}")
    print(f"Average Marks:{average:.2f}")
    print("." * 20)





