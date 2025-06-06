myFile = open ("number.txt", "rt")

list = []
for line in myFile:
    line = line.strip("\n")
    line = int(line)
    list.append(line)
    
    
print(list)