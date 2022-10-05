#Caesar Cipher

#index to pull from
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#menu
direction = input("Type 'encode' or 'decrypt' to either encode or decrypt a message:\n")
text = input("What is your message:\n").lower()
shift = int(input("How many shifts should be conducted on the message?:\n"))

#custom built shift adjustment for anything outside the index range of 25
if shift >= 25 and shift < 49:
  new_shift = shift - 25
elif shift >= 49:
  shift_less = shift - 2 
  new_shift = shift - shift_less
else: 
  new_shift = shift

#function to encrypt message
def encrypt (plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"Cipher Text is: {cipher_text}")

#function to decrypt message
def decrypt (cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    new_letter = alphabet[new_position]
    plain_text += new_letter
  print(f"Plain Text is: {plain_text}")

#option to choose encode or decrypt  
if direction == "encode":  
  encrypt(plain_text = text, shift_amount = new_shift)
elif direction == "decrypt":
  decrypt(cipher_text = text, shift_amount = new_shift)
else:
  print("You've entered an invalid entry")
