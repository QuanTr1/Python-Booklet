list = []
students = int(input("How many students in the class: "))
for i in range(1,students+1):
    student = input(f"What is student number {i} name: ")
    list.append(student)

c = int(input("What is the total number of periods of the class held in week (between 1 and 5): "))

while c > 5 or c < 1:
    print("Please enter a number between 1 to 5")
    c = int(input("What is the total number of periods of the class held in week (between 1 and 5): "))

for i in list:
    print(f"For student number {i}, {list[i]}")
    
    p = input(f"Enter attendance for {list[i]} (P/A) for period {i}: ")
    
    while p not in ("A" or "P"):
        print("Please enter \"A\" or \"P\"")
        p = input(f"Enter attendance for {list[i]} (P/A) for period {i}: ")
    
    