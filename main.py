import random, subprocess
def initGame(col, ro):
  # Also state the columns and rows of the game with params cos we may do multiple modes :>
  global numGuess, columns, rows, history, historyRW
  history = []
  historyRW = []
  columns, rows = col, ro
  # Generate the 5 digit number list
  numGuess = []
  for i in range (columns):
    numGuess.append(str(random.randint(0,9)))
  consDisplay("init")

def guessFunc():
  global guess, rightWrong
  for i in range (rows):
  # Make two lists – the right or wrong list and the input
  # List the input
  # Check for legible length
    rightWrong = []
    while True:
      guess = list(str(input("\033[0;0;40mGuess (" + str(columns) + " digits): ")))
      if len(guess) == columns:
        break
      elif len(guess) > columns:
        print("Too many characters have been used.")
      elif len(guess) < columns:
        print("Too little characters have been used.")
    # Index by index, compare the input with the current index -true-> put correct in right or wrong list; check for existence in list -true-> put some what in right or wrong list; 
    # not in list -> put wrong in right or wrong list.
    for i in range(columns):
      if guess[i] == numGuess[i]:
        rightWrong.append("c")
      elif guess[i] in numGuess:
          rightWrong.append("s")
      else:
          rightWrong.append("w")
    # If all are right, end the game!
    history.append(guess)
    historyRW.append(rightWrong)
    # Nest the guess and the data into a history list
    if not "s" in rightWrong and not "w" in rightWrong:
      consDisplay("correctGuess")
      break
    else:
      consDisplay("incorrectGuess")
      if len(history) == rows:
         consDisplay("lose")
         break

def consDisplay(varType):
  columnsEmpty = []
  for i in range (columns):
    columnsEmpty.append("[]")
  # Standard viewing / styling
  subprocess.run('clear', shell = True)
  print("\033[0;0;40m- - - - - Numberdle - - - - -")
  # Check the param, if its a incorrect guess:
  # Take in variables from outside and put it in a list
  # Display the previous guesses and empty boxes
  if varType == "incorrectGuess" or varType == "correctGuess" or varType == "lose":
    for i in range (len(history)):
        textColor(i)
    for i in range (rows - len(history)):
      print("\033[0;0;40m" + "         " + ("").join(columnsEmpty))
  # If the param is a correct guess:
  # Display the number and a string of text congratulating the user\
    if varType == "correctGuess":
      print("\033[0;0;40mCongratulation! You guessed the right number!")
      print((" ").join(guess))
    elif varType == "lose":
      print("\033[0;0;40m The code was: " + ("").join(numGuess))
  # Some nice UI for the start of the game :)
  elif varType == "init":
    for i in range (rows):
      print("\033[0;0;40m" + "         " + ("").join(columnsEmpty))

# Code has been debugged, the issue was that the space was being appended to the list "comp" too many times.
# ASCII text color handler issue resolved.

def textColor(index):
    # State variable, store in coparison lists
    comp = []
    comp.append("         ")
    # Print the number input with the color using conditions and the comparisons in the list
    for i in range(len(history[index])):
        # comp.append("         ")
        if historyRW[index][i] == "c":
            comp.append("\033[0;32;40m " + history[index][i])
        elif historyRW[index][i] == "s":
            comp.append("\033[0;33;40m " + history[index][i])
        elif historyRW[index][i] == "w":
            comp.append("\033[0;0;40m " + history[index][i])
    print(("").join(comp))
    # print(comp)

initGame(5,6)
guessFunc()
