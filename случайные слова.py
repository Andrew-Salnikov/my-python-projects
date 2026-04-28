# эта программа должна выводить список слов в случайном порядке 
import random
WORDS = ['доставка','спрайт','класс','пайтон']
x = 0
dell = []
while x < len(WORDS):
    word = random.choice(WORDS)
    if word not in dell:
        x += 1
        print(word)
        dell.append(word)
input('Press Enter to exit')