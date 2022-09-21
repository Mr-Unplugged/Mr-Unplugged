
import random

playerchoice = input("Pick a number from 1-3. 1 = Rock, 2 = Paper, 3 = Sissors.\n")

playerchoice_int = int(playerchoice)
computerchoice = random.randint(1,3)

compwin = "Computer wins"
playwin = "Player Wins"

if playerchoice_int == computerchoice:
    results = "its a tie"
elif playerchoice_int == 1 and computerchoice == 2: 
    results = compwin
elif playerchoice_int == 1 and computerchoice == 3: 
    results = playwin
elif playerchoice_int == 2 and computerchoice == 1: 
    results = playwin
elif playerchoice_int == 2 and computerchoice == 3:
    results = compwin
elif playerchoice_int == 3 and computerchoice == 1:
    results = compwin
else:
    results = playwin


if playerchoice_int == 1:
    print('''
    Player picks
     __
    /  |
    Rock! 

    ''')
elif playerchoice_int == 2:
    print('''
    Player picks
     ____
    |    |
    Paper! 

    ''')
elif playerchoice_int == 3:
    print('''
    Player picks

    8<
    Scissors!

    ''')
else: 
    print("That wasnt an option... nice")

if computerchoice == 1:
    print('''
    Computer picks
     __
    /  |
    Rock! 

    ''')
elif computerchoice == 2:
    print('''
    Computer picks
     ____
    |    |
    Paper! 

    ''')
else:
    print('''
    Computer picks

    8<
    Scissors!

    ''')

print(results)
