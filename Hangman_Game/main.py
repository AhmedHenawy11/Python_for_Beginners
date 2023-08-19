#STEP 1 - choose a random word and 
import random
import word_list
import art
from replit import clear
word = random.choice(word_list.word_list)
print(art.logo)
#STEP 2 - Make a blanks variable
blanks = []
for n in word:
    blanks += "_"
print(blanks)
#STEP3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word & replace with blank if exist  
life = 7
while blanks.count("_") > 0 :
  guess = input("Guess a letter: ").lower()
  clear()
  if guess in word :
    for position in range(len(word)):
      letter = word[position]
      if guess == letter:
        blanks[position] = letter 
  else:
    life -= 1
    print(art.stages[life])
    if life == 0:
      break
  print (blanks)

if "_" in blanks and life == 0:
  print("You lost.")
else:
  print("You won.")