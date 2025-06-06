#Ask for students, and periods held in class
students = int(input("How many students in the class: "))

    
periods = int(input("What is the total number of periods of the class held in week (between 1 and 5): "))
#While loop to check if the user input is between 1 and 5
while periods < 1 or periods > 5:
    print("Please enter a number between 1 and 5")
    periods = int(input("What is the total number of periods of the class held in week (between 1 and 5): "))
    
#Make a empty dictionary for students that store their attendance
students_data = {}

#for loop to ask for each of student's name 
for i in range(1,students + 1):
    name = input(f"Enter name for student {i}: ")
    while name == "":
        print("Please enter a student name.")
        name = input(f"Enter name for student {i}: ")
    
    #Make a list in the dictionary for each student to store their attendance
    students_data[name]= []
    
    #Ask for the attdentance 
    for a in range(1,periods + 1):
        attendance = input(f"Enter attendance for {name} (P/A) for period {a}: ")
        
        #While loop to check if the user enter a valid answer
        while attendance.upper() not in ["A", "P"]:
            print("Please enter \"A\" or \"P\"")
            attendance = input(f"Enter attendance for {name} (P/A) for period {a}: ")
        students_data[name].append(attendance.upper())


'''students_data = {'sahur': ['A','P','P','P'], 'tungtung' : ['A','A','A','P']}
periods = 4'''

print("Attendance Report:")

#Check for the students absents or presents and calculate the percentage.
#For loop to get student in the data
for student in students_data.keys():
    #set varibles for absent and present for each student
    absent = 0
    present = 0
    #for loop to get A or P in each of student list and +1 for absent or +1 for present
    for i in students_data[student]:
            if i == "A":
                absent += 1
            elif i == "P":
                present += 1
            else:
                absent += 1
    #calculate each student percentage
    percentage = present / periods * 100
    #if percentage is lower than 75 then warning for low attendance
    if percentage >= 75:       
        print(f"{student}: {present} periods presents({percentage:.0f}%)")
    else: 
        print(f"{student}: {present} periods presents({percentage:.0f}%) - Warning: Low attendance")

            
    
    
    
    

    


    