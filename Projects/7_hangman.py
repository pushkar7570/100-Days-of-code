import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["hangman", "mehul", "pushkar", "rajeev", "capture", "island", "shiv", "jai", "shree", "ram"]
word = random.choice(word_list)
word_len = len(word)

blank_word = []
for x in word:
    blank_word.append("_")
    
print(blank_word)  

lives = 6

while '_' in blank_word and lives >= 0:
    bool = 1
    letter = input("Guess the letter: ").lower()
    
    if letter in blank_word:
        print("You have already guessed this letter. Try another!!")
        continue
        
    for pos in range(word_len):
        if letter == word[pos]:
            bool = 0
            blank_word[pos] = letter
    
    if bool == 1:
        print(stages[lives])
        lives -= 1
        print(f"You are wrong and lost one life. Left : {lives+1}")
    
    print(blank_word)  
    
    if "_" not in blank_word:
        print("You win!!")
        break

            
            
