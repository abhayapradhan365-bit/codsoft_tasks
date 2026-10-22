import random
import string

letters = string.ascii_letters
digits = string.digits
special_characters = string.punctuation

all_characters = letters + digits + special_characters

length = int(input("Enter the desired password length: "))

password = ""

for i in range(length):
    password += random.choice(all_characters)

print("Generated Password:", password)