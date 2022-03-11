#dynamic solution, fruit version

import urllib.request
import json
import io
import random

list = urllib.request.urlopen("https://raw.githubusercontent.com/dariusk/corpora/master/data/foods/fruits.json")

listread = list.read()

fruitsList = json.loads(listread.decode("utf-8"))["fruits"]

solution_index = random.randint(0, (len(fruitsList)-1))

solution = fruitsList[solution_index]

solution_length = len(solution)

guess_count = 0
print("Welcome to fruitle! You will have six guesses to guess the fruit of the day. If you want to give up, you can type 'give up'.")
print("Today's fruit has " + str(solution_length) + " letters.")
while guess_count <= 6:
  guess = input("What is your guess? ")
  guess = str.lower(guess)
  if guess == "give up":
    print("Okay, we can stop.")
    print("The fruitle was " + solution + ".")
    break
  elif len(guess) != solution_length:
    print("Your guess should be " + str(solution_length) + " letters.")
  elif guess == solution:
    print("You got the fruitle!")
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
  print("You did not get the fruitle today.")
  print("The fruitle was " + solution + ".")
  print("See you later!")
