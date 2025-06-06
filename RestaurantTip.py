people = int(input("How many people are there? "))
percentage =int(input("How much percentage do you want to tip? "))
bill = float(input("How much the bill come? "))
miles = float(input("What is the distance you have to travel? "))
total = miles * 0.45 + bill * (1+(100/percentage))

print(f'Each person has to pay ${total / people}')


