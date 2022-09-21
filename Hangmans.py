#hangman

#import
from dis import dis
import random
from tkinter import N
from turtle import clear
from Hangman_Stages import stages

#global variables
game = 1
length_of_word = 0
display_list = []
lives = 6

#list of random words
words_to_guess = ["Dog", "Cat", "Mouse", "Horse", "Pony", "Skunk", "Poop", "Fox", "DeerFox"]

#selecting random word
selected_word = random.choice(words_to_guess)
selected_word = selected_word.lower()

#print(selected_word)

end_of_game = False

#displays "_" for each letter of the selected word
for let in selected_word:
        display_list += "_"

#title screen
print(''' 
-= Welcome to Hangman! =-
''')

print(f"The current word is {display_list}\n")

#While loop with end of game variable set as false initially until certain critera is met. 
while end_of_game == False:

    #player input
    guess = input("Guess a letter!: ").lower()
    

    #if the guess is correct
    for position in range(len(selected_word)):
        #letter is equal to any of the positions
        letter = selected_word[position]
        #if one of the letters is equal to the guess
        if letter == guess:
            #display the correct letter in the correct position
            display_list[position] = letter
            #show the hangman
            print(stages[lives])
            #tell the user they have x number of lives left
            print(f"You have {lives} lives left!\n")
        
    #if the guess is incorrect    
    if guess not in selected_word:
        #subtract a life
        lives -= 1
        #show the hangman
        print(stages[lives])
        #tell the user they have x number of lives left
        print(f"The letter {guess} is not in the word. You have {lives} lives left!\n")

    print(f"{display_list}\n")

    #break the loop if
    if "_" not in display_list:
        end_of_game = True
        print("You've won!")
    elif lives == 0:
        end_of_game = True
        print("You've lost!")
    

