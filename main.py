from password_generator import generate_password
from password_encryption import encrypt

password = encrypt(generate_password(lenght=20, useLowerCase=True, useCapital=True, useNumbers=True, useSpecial=True))

with open(".dbfiles.txt", 'a') as f:
    f.write(str(password))