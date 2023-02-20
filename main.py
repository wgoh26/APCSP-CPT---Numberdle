import random, sys, subprocess
def initGame(col, ro):
  # Also state the columns and rows of the game with params cos we may do multiple modes :>
  global numGuess, columns, rows
  columns, rows = col, ro

  # Generate the 5 digit number list
  numGuess = []
  for i in range (columns):
    addNum = random.randint(0,9)
    numGuess.append(str(addNum))
  print(numGuess)


def guessFunc():
  global guess, history, rightWrong, historyRW
  history = []
  historyRW = []
  for i in range (rows):
  # Make two lists – the right or wrong list and the input
  # List the input
  # Check for legible length
    rightWrong = []
    while True:
      guess = list(str(input("Guess (" + str(columns) + " digits): ")))
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
      else:
        if guess[i] in numGuess:
            rightWrong.append("s")
        else:
            rightWrong.append("w")

    # If all are right, end the game!
    if "c" in rightWrong and not "s" in rightWrong and not "w" in rightWrong:
      consDisplay("correctGuess")
      break
    else:
      consDisplay("incorrectGuess")



def consDisplay(varType):
  tries = 0
  tries += 1
  columnsEmpty = []

  for i in range (columns):
    columnsEmpty.append("[]")

  # Check the param, if its a incorrect guess:
  # Take in variables from outside and put it in a list
  # Display the previous guesses and empty boxes
  if varType == "incorrectGuess":
    subprocess.run('clear', shell = True)
    history.append(guess)
    historyRW.append(rightWrong)
    print("- - - - - Numberdle - - - - -")
    for i in range (len(history)):
    #   print("         " + history[i])
        textColor(i)
    for i in range (rows - len(history)):
      print("\033[0;0;40m" + "         " + ("").join(columnsEmpty) + "\033[0")
  # If the param is a correct guess:
  # Display the number and a string of text congratulating the user\
  elif varType == "correctGuess":
    subprocess.run('clear', shell = True)
    print("- - - - - Numberdle - - - - -")
    print("Congratulation! You guessed the right number!")
    print((" ").join(guess))

  elif varType == "lose":
    subprocess.run('clear', shell = True)
    history.append(guess)
    historyRW.append(rightWrong)
    print("- - - - - Numberdle - - - - -")
    for i in range (len(history)):
    #   print("         " + history[i])
        textColor(i)
    for i in range (rows - len(history)):
      print("\033[0;0;40m" + "         " + ("").join(columnsEmpty) + "\033[0")


def textColor(index):
    # State variable, store in coparison lists
    comp = []
    # Print the number input with the color using conditions and the comparisons in the list
    for i in range(len(history[index])):
        comp.append("         ")
        if historyRW[index][i] == "c":
            comp.append("\033[0;32;40m " + history[index][i] + "\033[0")
        elif historyRW[index][i] == "s":
            comp.append("\033[0;33;40m " + history[index][i] + "\033[0")
        elif historyRW[index][i] == "w":
            comp.append("\033[0;0;40m " + history[index][i] + "\033[0")
    print(("").join(comp))

initGame(5,6)
guessFunc()