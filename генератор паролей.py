import random
letter = "qwertyuiopasdfghjklzxcvbnm"
number = "1234567890"
symbol = "!@#$%^&*()-/"
letter_u = "QWERTYUIOPASDFGHJKLZXCVBNM"
all = letter + number + symbol + letter_u
password = ""
for i in range(12):
    password += random.choice(all)
print(password)