import random
logo = """
  ___  __  __  ____  ___  ___    ____  _   _  ____    _  _  __  __  __  __  ____  ____  ____ 
 / __)(  )(  )( ___)/ __)/ __)  (_  _)( )_( )( ___)  ( \( )(  )(  )(  \/  )(  _ \( ___)(  _ \
( (_-. )(__)(  )__) \__ \\__ \    )(   ) _ (  )__)    )  (  )(__)(  )    (  ) _ < )__)  )   /
 \___/(______)(____)(___/(___/   (__) (_) (_)(____)  (_)\_)(______)(_/\/\_)(____/(____)(_)\_)
"""
print(logo)

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
random_num = random.randint(1,100)
print(f"Pstt.. the correct answer is {random_num}")
diff_choice = input("Choose a difficulty. Type 'easy' or 'hard'. ").lower()

if diff_choice == 'hard':
  no_of_lives = 5
else:
  no_of_lives = 10

flag = 0

while no_of_lives >= 1:
  print(f"You have {no_of_lives} attempts remaining to guess the number.")
  guessed_num = int(input("Make a guess: "))
  if guessed_num == random_num:
    print(f"You got it! The answer was {random_num}.")
    flag = 0
    break
    
  elif guessed_num > random_num:
    print("Too high. \nGuess again.")
    no_of_lives -= 1
    flag = 1
    
  else:
    print("Too low. \nGuess again.")
    no_of_lives -= 1
    flag = 1

if flag == 1:
  print("You've run out of guesses, you lose.")
