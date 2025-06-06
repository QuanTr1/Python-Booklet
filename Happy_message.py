happy = int(input("How happy are you from the scale between 1 and 10? "))
if happy <= 3:
    print("You are sad")
elif happy >= 4 and happy <=7:
    print("You are netural/happy")
elif happy >=8:
    print('You are very happy')
print("Have a good day")