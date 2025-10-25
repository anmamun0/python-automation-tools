import random
import string

def generate_password(length):
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    return password


length = 16 # change this to desired password length
password = generate_password(length)

print(password)
