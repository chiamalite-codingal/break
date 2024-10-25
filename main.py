word = input("Enter word:")
for i in word:
    if i=="U" or i=="u":
        print("Found u")
        break
    else:
        print("Not found")