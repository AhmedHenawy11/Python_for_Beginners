#STEP1 - choose a random word and 
import random
word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)
print(word)
#STEP 2 - Make a blanks variable
blanks = []
for n in word:
    blanks += "_"
print(blanks)
#STEP3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word & replace with blank if exist  
life = 3
while blanks.count("_") > 0 :
  guess = input("Guess a letter: ").lower()
  lenth = 0
  if word.count(guess) > 0:
    for letter in word:
      lenth+=1
      if guess == letter:
        blanks[lenth-1] = letter 
  else:
    life -= 1
    if life == 0:
      break
  print (blanks)
  print(f"You have {life} left")

if blanks.count("_") > 0 and life == 0:
  print("You lost.")
else:
  print("You won")