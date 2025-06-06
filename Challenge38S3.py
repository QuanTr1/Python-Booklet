myFile = open("number.txt", "at")   # opens the file for appending (adding to)
for a in range (4):
    newNo = input("Please enter new number")
    myFile.write(str(newNo)+"\n")  # converts the integer to a string & adds a newline instruction
myFile.close()
