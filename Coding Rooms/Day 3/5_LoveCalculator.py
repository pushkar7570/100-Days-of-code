# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
cost1 = 0
cost2 = 0
name = name1 + name2
for x in ("trueTRUE"):
    for y in name:
        if(x == y):
            cost1 += 1

for x in ("loveLOVE"):
    for y in name:
        if(x == y):
            cost2 += 1            

res = cost1*10 + cost2
if(res<10 or res>90):
    print(f"Your score is {res}, you go together like coke and mentos.")
elif(res<=50 and res>=40):
    print(f"Your score is {res}, you are alright together.")
else:
    print(f"Your score is {res}.")
