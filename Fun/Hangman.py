import random
from words import words
from hangman_visual import lives_visual_dict # Optional
import string

def get_valid_word(words):
  word = random.choice(words)
  while '-' in word or ' ' in word:
    word = random.choice(words)
  return word.upper()

def hangman():
  word = get_valid_word(words)
  word_letters = set(word)  # Letters in the word
  alphabet = set(string.ascii_uppercase)
  used_letters = set()  # What the user has guessed

  lives = 7  # For limited chances

  # Getting user input
  while len(word_letters) > 0 and lives > 0:  # For limited chances
    
    # Letters used
    # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
    print("You have", lives, "lives left")  # For limited chances
    print("You have used these letters: ", ' '.join(used_letters))

    # What current word is (ie W - R D)
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print("Current word: ", ' '.join(word_list))
    
    user_letter = input("\nGuess a letter: ").upper()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
      else:
        lives = lives - 1  # For limited chances
        print(lives_visual_dict[lives])  # Optional
        print("Letter is not in word!!")
  
    elif user_letter in used_letters:
      print("You have already used that character, PLEASE TRY AGAIN!!")
  
    else:
      print("Invalid character, PLEASE TRY AGAIN!!")
  # Gets here when len(word_letters) == 0 OR when lives == 0
  if lives == 0:
    print("Sorry, You died. Better LUCK next time!!")
    print("The word was", word)
  else:
    print("Congratulations, you guessed the word", word, "!!")

if __name__ == '__main__':
  hangman()