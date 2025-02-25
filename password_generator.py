from random import choice
from string import ascii_letters, ascii_lowercase

def generate_password(lenght: int, useLowerCase: bool, useNumbers: bool, useSpecial: bool, useCapital: bool):
    numbers = '0123456789'
    specials = "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    password = ''
    pool = ''

    if(useCapital):
        pool += ascii_letters
    if(useLowerCase and not(useCapital)):
        pool += ascii_lowercase
    if(useNumbers):
        pool += numbers
    if(useSpecial):
        pool += specials

    while lenght > 0:
        password += choice(pool)   
        lenght -= 1

    return password
