men = {"James", "Peter"}

# Initialize counters
total_w = total_h = total_count = 0
men_w = men_h = men_count = 0
women_w = women_h = women_count = 0

with open("people.txt") as file:
    for line in file:
        name, w, h = line.strip().split(",")
        w, h = float(w), float(h)

        # Overall totals
        total_w += w
        total_h += h
        total_count += 1

        # Gender-specific totals
        if name in men:
            men_w += w
            men_h += h
            men_count += 1
        else:
            women_w += w
            women_h += h
            women_count += 1

# Calculate averages
overall_avg = (total_w / total_count, total_h / total_count)
men_avg = (men_w / men_count, men_h / men_count)
women_avg = (women_w / women_count, women_h / women_count)

# Output
print(f"Overall average weight: {overall_avg[0]} kg")
print(f"Overall average height: {overall_avg[1]} m\n")
print(f"Men's average weight: {men_avg[0]} kg")
print(f"Men's average height: {men_avg[1]} m\n")
print(f"Women's average weight: {women_avg[0]:.1f} kg")
print(f"Women's average height: {women_avg[1]:.2f} m")
