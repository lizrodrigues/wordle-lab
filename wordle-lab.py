#manual solution setting version

solution = "cat"
guess_count = 0
print("Welcome to my wordle! In this wordle, you will have six guesses to guess a three letter word.")
while guess_count <= 6:
  guess = input("What is your guess? ")
  guess = str.lower(guess)
  if len(guess) != 3:
    print("Your guess should be three letters.")
  elif guess == solution:
    print("You got the wordle!")
    break
  else:
    right_spot = ""
    right_letter = ""
    not_in = ""
    for letter in range(len(guess)):
      if guess[letter] == solution[letter]:
        right_spot = right_spot + guess[letter]
      if guess[letter] != solution[letter] and guess[letter] in solution:
        right_letter = right_letter + (guess[letter])
      if guess[letter] not in solution:
        not_in = not_in + (guess[letter])
    print("These letters were in the right spot:")
    print([right_spot])
    print("These letters are in the answer but not in the right spot:")
    print([right_letter])
    print("These letters are not in the answer:")
    print([not_in])
    guess_count += 1

if guess_count > 6:
  print("You did not get the wordle today. See you tomorrow!")
