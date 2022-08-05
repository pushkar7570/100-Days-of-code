print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))
total_bill += total_bill * tip_percent/100
bill_per_person = round((total_bill / no_of_people), 2)
# you can use format function also 
# bill_per_person = "{:.2f}".format(total_bill / no_of_people)

print(f"Each person should pay: ${bill_per_person}")
