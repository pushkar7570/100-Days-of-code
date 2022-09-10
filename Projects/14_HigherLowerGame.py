#content of both files art.py and game_data.py has been commented below.
from art import logo, vs 
from game_data import data
from replit import clear
import random

def compare(accOne, accTwo):
  """ Function to print the properties of both accounts and compare the two chosen accounts and return the result accordingly. """
  
  print(f"Compare A: {accOne['name']}, a {accOne['description']}, from {accOne['country']}.")
  print(vs)
  print(f"Against B: {accTwo['name']}, a {accTwo['description']}, from {accTwo['country']}.")
  
  if accOne['follower_count'] > accTwo['follower_count'] :
    return 'a'
  else:
    return 'b'

print(logo) 

wrong_answer = False 
score = 0
accOne = random.choice(data) 
accTwo = random.choice(data)

if accOne['follower_count'] == accTwo['follower_count']:
  #checking if the second randomly chosen account has the same followers. If yes, then assigning new value again.
  accTwo = random.choice(data)

answer = compare(accOne, accTwo)

while wrong_answer is False:
  choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  if answer == choice:
    clear()
    print(logo)
    score += 1
    print(f"You're right! Current Score: {score}.")
    accOne = accTwo
    accTwo = random.choice(data) 
    if accOne['follower_count'] == accTwo['follower_count']:
      accTwo = random.choice(data)
    answer = compare(accOne, accTwo)
   
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final Score: {score}")
    wrong_answer = True
    
        
    
