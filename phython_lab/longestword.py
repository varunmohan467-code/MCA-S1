llist=input("Enter a list of words seperated by spaces:").split(" ")
longest_length=0
for word in llist:
    if len(word)>longest_length:
        longest_length=len(word)
        long_word=word
        print("THe longest word is",long_word)
        print("THe length of the longest word is:",longest_length)