
# Name: Luke Mauser
# Class: CSCI110
# Date: 5-16-2024

def beginning():
  import random

  import sys

  import os

  # simple intro
  print("Hello! Welcome to H A N G M A N")
  print("\n r---+")
  print(" o   |")
  print("/|\  |")
  print("/ \  |")
  print("     ///")
  print("<<<<<>>>>>>")

  #user must decide to play
  def start():
    g = input("Ready to play? [y/n]: ")
    if "y" in g:
      pass
    if "n" in g:
      print("\nCome back another time!")
      print("\nG A M E O V E R")
      os.execl(sys.executable, sys.executable, *sys.argv)

  start()

  # word bank for the game to randomly select from
  # wordsfile = open("wordbank.py", "r")
  # wordBank = wordsfile.readlines()
  ## I could not figure out the wordBank with
  ## File IO but above was my attempt, 
  ## however it did not work.

  # choose a random word
  wordBank = ("heart", "crow", "basketball", "jackpot","starship","yellow", "green", "video", "coding", "movies", "dictionary", "computer", "index", "vitamins", "zebra", "porcupine", "dinosaur", "cheese", "hippopotamus", "tiger", "bear", "lettuce")

  randomWord = random.choice(wordBank)

  # amount of spaces for the random word
  for x in randomWord:
     print("_", end=" ")

  # prints out the word when guessed
  def outputLetters(guesses):
    counter = 0
    correct = 0
    for char in randomWord:
      if char in guesses:
        print(randomWord[counter], end=" ")
        correct+=1
      else:
        print(" ", end=" ")
      counter+=1
    return correct

  # repeats the dashes under the characters in the random word
  def dashes():
    print("\r")
    for char in randomWord:
      print("-", end=" ")

  
  length_of_word = len(randomWord)
  wrong_guesses = 0
  current_guess_index = 0
  current_letters_guessed = []
  right_guesses = 0

  # making the drawing for each wrong guess
  def hangman_drawing(wrong):
    if(wrong == 0):
      print("\nr---+")
      print("    |")
      print("    |")
      print("    |")
      print("    ///")
      print("<<<<<>>>>>>")
    # every wrong guess adds a limb
    elif(wrong == 1): 
      print("\nr---+")
      print("o   |")
      print("    |")
      print("    |")
      print("    ///")
      print("<<<<<>>>>>>")
    elif(wrong == 2):
      print("\nr---+")
      print("o   |")
      print("|   |")
      print("    |")
      print("    ///")
      print("<<<<<>>>>>>")
    elif(wrong == 3):
      print("\nr---+")
      print(" o  |")
      print("/|  |")
      print("    |")
      print("    ///")
      print("<<<<<>>>>>>")
    elif(wrong == 4):
      print("\nr---+")
      print(" o  |")
      print("/|\ |")
      print("    |")
      print("    ///")
      print("<<<<<>>>>>>")
    elif(wrong == 5):
      print("\nr---+")
      print(" o  |")
      print("/|\ |")
      print("/   |")
      print("    ///")
      print("<<<<<>>>>>>")
    elif(wrong == 6):
      print("\nr---+")
      print(" o   |")
      print("/|\  |")
      print("/ \  |")
      print("    ///")
      print("<<<<<>>>>>>")


  while(wrong_guesses != 6 and right_guesses != length_of_word):
    print("\nLetters guessed: ")
    for letter in current_letters_guessed:
      print(letter, end=" ")
    # prompt to guess a letter
    letterGuessed = input("\nGuess a new letter!: ")
    # user is right
    if letterGuessed in randomWord:
      hangman_drawing(wrong_guesses)
      print("\n                Nice Guess!")
      # print word
      current_guess_index+=1
      current_letters_guessed.append(letterGuessed)
      right_guesses = outputLetters(current_letters_guessed)
      dashes()
    # user was wrong
    else:
      wrong_guesses+=1
      current_letters_guessed.append(letterGuessed)
      # add a limb
      hangman_drawing(wrong_guesses)
      print("\n                Try Again!")
      # print word
      right_guesses = outputLetters(current_letters_guessed)
      print("     You have {0} attempts left".format(6 - wrong_guesses))
      dashes()

  # reveals the random word once they lose
  def failed():
    if wrong_guesses == 6:
      print("     The word was " + randomWord + ".")

  failed()
  # ask if the user wants to play again
  def end():
      f = input("\nWant to play again? [y/n]: ")
      if "y" in f:
          beginning()
      if "n" in f:
          print("\nThanks for playing!")
          print("\nG A M E O V E R")
          print("-----------------------------------")
          pass

  def test(did_pass):
      """  Print the result of a test.  """
      linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
      if did_pass:
          msg = "Test at line {0} ok.".format(linenum)
      else:
          msg = ("Test at line {0} FAILED.".format(linenum))
      print(msg)       

  end()

  test(beginning)

  
  test(failed)
      
    
       

beginning()