from operator import length_hint
import random
from typing import final

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%']

print("Welcome to the random password generator!")
Length = int(input("How long should your password be *Hint* It should be at least 14 characters long!"))
Number_Length = int(input("How many numbers should it have? *Hint* It should have at least 2 numbers!"))
Special_Characters = int(input("How many Special Charaters should it have? *Hint* It should have at least 2 special charaters!"))

password = []
final_password = ""

for char in range (1, Length + 1):
    random_char = random.choice(letters)
    #print (random_char)
    password += random_char

for num in range (1, Number_Length + 1):
    random_number = random.choice(numbers)
    #print (random_number)
    password += random_number

for sym in range (1, Special_Characters + 1):
    random_scharacter = random.choice(symbols)
    #print (random_scharacter)
    password += random_scharacter

#print(password)

random.shuffle(password)

for char in password:
    final_password += char

print (f"Final password is: {final_password}")
