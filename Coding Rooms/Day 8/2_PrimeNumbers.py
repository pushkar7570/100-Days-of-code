#Write your code below this line 👇
import math
def prime_checker(number):
    flag = True
    rounded_root_of_number = math.ceil(math.sqrt(number))
    for x in range(2, rounded_root_of_number):
        if number % x == 0:
            flag = False
    if flag is True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")    



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
