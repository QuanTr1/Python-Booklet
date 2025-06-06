age = int(input("what is your age: "))
is_student_input = input("Are you a student of Copperfield College(yes/no): ")
is_student = is_student_input.lower()== "yes"

if is_student :
    if age >= 15:
        print("You are in middle school or above")
        
    else:
        print("Have a nice day Copperfield College Student")
        

else:
    print("Have a nice day")