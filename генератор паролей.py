import random
number = '1234567890'
letter = 'qwertyuiopasdfghjklzxcvbnm'
letter_1 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
symbols = '!@#$%^&*?/'
all = number + letter + letter_1 + symbols
password = ''
for i in range(12):
    password += random.choice(all)
print(password)