# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
left = 90-int(age)
days = str(left*365)
weeks = str(left*52)
months = str(left*12)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
