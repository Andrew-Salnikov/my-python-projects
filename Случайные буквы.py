import random
word = 'индекс'
print(f'В переменной word хранится слово: {word}')
low = -len(word)
high = len(word)
for i in range (5):
    position = random.randrange(low, high)
    print(f'word [ {position} ]\t {word[position]}')
input('\n\t\t\tPress Enter to exit')
