#Hangman
#You know how hangman works


#hangman art helper function
#random word picker
import random


def randWordPicker():
  wordList = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
  return random.choice(wordList)



def mainFunc():
  print("Welcome to HANGMAN!")
  print("Guess the correct word in time to keep your stick figure character alive!")
  print("Good Luck!")
  print("")
  
  randomWord = randWordPicker()
  boardDisplay("", randomWord, "", 0)

  guessesSoFar = []
  correctGuesses = []
  numCorrectGuesses = 0
  wrongGuesses = []
  numWrongGuesses = 0

  while True:
    currentGuess = makeAGuessGuy(guessesSoFar)
    guessesSoFar = guessesSoFar + [currentGuess]
    if currentGuess in randomWord:
      correctGuesses = correctGuesses + [currentGuess]
      numCorrectGuesses = numCorrectGuesses + randomWord.count(currentGuess)
    else:
      wrongGuesses = wrongGuesses + [currentGuess]
      numWrongGuesses = numWrongGuesses + 1

    boardDisplay(wrongGuesses, randomWord, correctGuesses, numWrongGuesses)

    if numWrongGuesses == 6:
      print("")
      print("")
      print("You Lose. Better luck next time!!")
      return None
    elif numCorrectGuesses == len(randomWord):
      print("")
      print("")
      print("You Win!! Have a cookie.")
      return None



HANGMANpICKS = ['''
  +---+
      |
      |
      |
    ===''', '''
  +---+
  O   |
      |
      |
    ===''', '''
  +---+
  O   |
  |   |
      |
    ===''', '''
  +---+
  O   |
 /|   |
      |
    ===''', '''
  +---+
  O   |
 /|\  |
      |
    ===''', '''
  +---+
  O   |
 /|\  |
 /    |
    ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
    ===''']

def wrongGuessesIndicator(wrongGuesses):
  print("Wrong Guesses:")
  print("")
  for i in range(len(wrongGuesses)):
    print(wrongGuesses[i]+ " ",end="")



def makeAGuessGuy(guessesSoFar):
  guess = str(input("Pick a letter, any letter.   "))
  if guess not in guessesSoFar:
    return guess
  else:
    print("You already guessed this letter, silly!")
    print("Try again.")
    makeAGuessGuy(guessesSoFar)


def boardDisplay(wrongGuesses, currentWord, correctGuesses, numWrongGuesses):
  print(HANGMANpICKS[numWrongGuesses])
  wordLength = len(currentWord)
  wrongGuessesIndicator(wrongGuesses)
  print("")
  print("")
  print("")
  currentAnswer = ""
  for j in range(len(currentWord)):
    letterMatchFlag = False
    for i in range(len(correctGuesses)):
      if correctGuesses[i] == currentWord[j]:
        letterMatchFlag = True

    if letterMatchFlag == True:
      currentAnswer = currentAnswer + currentWord[j] + " "
    else:
      currentAnswer = currentAnswer + "_ "

  print(currentAnswer)

mainFunc()
