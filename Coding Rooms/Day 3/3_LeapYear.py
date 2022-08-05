# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if((year%4==0 and year%100!=0) or year%400==0 ):
    print("Leap year.")
else:
    print("Not leap year.")
    
# or you can use the below code

# if year % 4 != 0:
#     print("Not leap year.")
# else:
#     if year % 100 != 0:
#         print("Leap year.")
#     else:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.") 
