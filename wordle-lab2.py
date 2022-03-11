#five letter dynamic solution

import urllib.request
import json
import io
import random

list = urllib.request.urlopen("https://raw.githubusercontent.com/lizrodrigues/wordle-lab/main/wordle-guesses.json")

  #Six letter guess list option: "https://raw.githubusercontent.com/jakerella/guessle/main/lists/scrabble_6.json"

listread = list.read()

wordList = json.loads(listread.decode("utf-8"))

solution_index = random.randint(0, (len(wordList)-1))

solution = wordList[solution_index]

solution_length = len(solution)

guess_count = 0
print("Welcome to budget wordle! You will have six guesses to guess the word of the day. If you want to give up, you can type 'give up'.")
print("Today's word has " + str(solution_length) + " letters.")
while guess_count <= 6:
  guess = input("What is your guess? ")
  guess = str.lower(guess)
  if guess == "give up":
    print("Okay, we can stop.")
    print("The wordle was " + solution + ".")
    break
  elif len(guess) != solution_length:
    print("Your guess should be " + str(solution_length) + " letters.")
  elif guess == solution:
    print("You got the wordle!")
    break
  else:
    full_answer = ""
    right_letter = ""
    not_in = ""
    for letter in range(len(guess)):
      if guess[letter] == solution[letter]:
        full_answer = full_answer + guess[letter]
      if guess[letter] != solution[letter] and guess[letter] in solution:
        full_answer = full_answer + "_"
        right_letter = right_letter + (guess[letter])
      elif guess[letter] not in solution:
        full_answer = full_answer + "_"
        not_in = not_in + (guess[letter])
    print("These letters were in the right spot:")
    print([full_answer])
    print("These letters are in the answer but not in the right spot:")
    print([right_letter])
    print("These letters are not in the answer:")
    print([not_in])
    guess_count += 1

if guess_count > 6:
  print("You did not get the wordle today.")
  print("The wordle was " + solution + ".")
  print("See you later!")
