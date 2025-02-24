from random import choice, random
from string import ascii_letters, ascii_lowercase

letters = []
lowercaseLetters = []
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in ascii_letters:
    letters.append(i)
for i in ascii_lowercase:
    lowercaseLetters.append(i)

def generate_password(lenght: int, useCapital: bool, useNumbers: bool):
    password = ''
    while lenght > 0:
        if(useNumbers):
            randomNumber = round(random())
            if(randomNumber):
                password += choice(numbers)
            else:
                if(useCapital):
                    randomCapital = round(random())
                    if(randomCapital):
                        password += choice(letters)
                else:
                    password += choice(lowercaseLetters.split())
        lenght -= 1
    print(password)
    return password

