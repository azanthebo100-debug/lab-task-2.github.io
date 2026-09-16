print("Pay calculator")

pay = float(input("Enter pay per hour: "))
hour = float(input("Enter hours: "))

if hour <= 40:
    earned = pay * hour
else:
    extratime = hour - 40
    earned = (pay * 40) + (extratime * pay * 1.5)

print(f"Your earned money is {earned}")