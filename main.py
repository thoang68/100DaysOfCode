#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
try:
  import random
  import art
  print(art.logo)
  level=input("Type \"H\" for Hard and \"E\" for Easy: ").upper()
  if level=="H":
    guesses=5
    print("You have 5 attempts to guess a number.")
  elif level=="E":
    guesses=10
    print("You have 10 attempts to guess a number.")
  else: 
    print("Invalid input!")
    exit()

  
  actual_number=random.randint(1,100)
  def guess_game(guess_num,actual_num):
    if guess_num < actual_num:
      return "Low"
    elif guess_num > actual_num:
      return "High"
    else:
      return "Correct"
  print(actual_number)

  for i in range(guesses):
    
    guess_number=int(input("Guess a number between 1 and 100: "))
    result=guess_game(guess_number,actual_number)
    guesses_left=guesses-i-1
    if result=="Low" or result=="High":
      if guesses_left==1:
        print(f"Your guess number is Too {result}! WATCH OUT! You only have {guesses_left} guess left.")
      elif guesses_left==0:
        print(f"Your guess number is Too {result}! Sorry! You have no more guesses! The correct number is {actual_number}")
      else:
        print(f"Your guess number is Too {result}! You have {guesses_left} guesses left.")
 
    else:
      print(f"You win! {guess_number} is the correct one!")
      quit()
  
except:
  pass



  