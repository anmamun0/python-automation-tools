import random

def generate_password(digit):
    password = ''.join(random.sample(digit, len(digit)))
    return password

digit = "12345678" # change this to desired digit
password = generate_password(digit)
print(password)
