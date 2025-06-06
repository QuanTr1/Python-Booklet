import math
pictures = int(input("How much pictures would you use each month? "))
texts = int(input("How much texts would you use each month? "))
data = int(input("How much data(MB) would you use each month? "))

bills = pictures * 0.35 + texts * 0.10 + data * 0.05

if bills > 10:
    print("You better on a contract")
    
cost = math.ceil(data/500) * 2.50

print(f"The cost for {data}MB is ${cost}")