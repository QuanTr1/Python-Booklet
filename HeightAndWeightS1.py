# Step 1: The fixed version of your list (with strings)
data = ["James", 73, 1.82,
        "Peter", 78, 1.80,
        "Beth", 65, 1.53,
        "Mags", 66, 1.50,
        "Joy", 62, 1.34]

# Step 2: Save data to a file
with open("people.txt", "w") as file:
    for i in range(0, len(data), 3):
        file.write(f"{data[i]},{data[i+1]},{data[i+2]}\n")