myFile = open("number.txt", "wt")

list = []
for i in range(6):
    number = int(input("Enter the a number: "))
    list.append(number)
list.sort()
print(list)
for item in list:
    myFile.write(f"{item}\n")
myFile.close() 
