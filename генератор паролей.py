import random
letter = "qwertyuiopasdfghjklzxcvbnm"
number = "1234578"
letter_u = "QWERTYUIOPASDFGHJKLZXCVBNM"
symbol = "!@#$%^&*"
all = letter + number + letter_u + symbol
password = ""
x = int(input("Введите длину желаемого пароля: "))
for i in range(x):
    password += random.choice(all)

print(f"Ваш сгенерированный пароль: {password} . ")
