import bcrypt

def encrypt(password: str):
    hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hash