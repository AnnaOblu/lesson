import random
import string

adjectives = ['cubic', 'fragrant', 'rough', 'wet', 'calm', 'hairy',
              'sleepy', 'slow', 'hot', 'cold', 'big', 'red', 'orange',
              'yellow', 'green' ]
nouns = ['apple', 'dinosaur', 'ball', 'goat', 'dragon', 'car', 'car',
         'eggplant ', 'jelly', 'sugar', 'avocado']
while True:
    for num in range(3):
        print('Добро пожаловать')
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(1, 100)
        special_char = random.choice(string.punctuation)
        password = adjective + noun + str(number) + special_char
        print('Новый пароль: ' + password)
    response = input('Сгенирировать новый пароль? Введите д или н')
    if response == 'н':
        break





