import random
from replit import clear
from art import logo


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards_list):
  if sum(cards_list) == 21 and len(cards_list) == 2:
    return 0
    
  if 11 in cards_list and sum(cards_list) > 21:
    cards_list.remove(11)
    cards_list.append(1)
  return sum(cards_list)


def compare(user_score, comp_score):
  if user_score > 21 and comp_score > 21:
    print("You lose.")
  if user_score == comp_score:
    print("It's a draw.")
  elif comp_score == 0 or user_score > 21:
    print("Computer Wins.")
  elif user_score == 0 or comp_score > 21:
    print("User Wins.")
  elif user_score > comp_score:
    print("User Wins.")
  else:
    print("Computer Wins.")


def play_game():
  print(logo)

  user_cards = []
  computer_cards = []
  game_end = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not game_end:
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(computer_cards)
    print(f"Your cards : {user_cards} and score: {user_score}")
    print(f"Compuer's first card: {computer_cards[0]}")

    if user_score == 0 or comp_score == 0 or user_score > 21:
      game_end = True
    else:
      user_choice = input("Type 'y' to draw another card and 'n' to pass. ")
      if user_choice == 'y':
        user_cards.append(deal_card())
      else:
        game_end = True

  while comp_score != 0 and comp_score < 17:
    computer_cards.append(deal_card())
    comp_score = calculate_score(computer_cards)

  print(f"Your final cards: {user_cards} , final score: {user_score}")
  print(f"Computer final cards: {computer_cards} , final score: {comp_score}")
  compare(user_score, comp_score)

while input("Do you want to play a Blackjack game? Type 'y' to play and 'n' to exit. ") == "y" :
  clear()
  play_game()
