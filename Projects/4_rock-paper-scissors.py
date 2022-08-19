import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
allChoices = ["Rock" , "Paper" , "Scissors"]

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print("Your choice: " + allChoices[userChoice])

compChoice = random.randint(0,2)
print("Computer choice: " + allChoices[compChoice])

if userChoice < 0 or userChoice >= 3 :
  print("Enter valid number.")
elif userChoice == compChoice:
  print("Its a draw.")
elif userChoice == 0 and compChoice == 2:
  print("You win.")
elif userChoice == 2 and compChoice == 1:
  print("You win.")
elif userChoice == 1 and compChoice == 0:
  print("You win.")
else:
  print("You lose.")
