import random
import string

lenght = int(input("Desired password lenght: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(lenght))
print("Your password is",password)
