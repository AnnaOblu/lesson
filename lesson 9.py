import random
with open('passwords') as f:
    passwords_data = f.read()


class BadPasswordGenerator:
    def __init__(self):
        self.i = 0
        self.passwords = passwords_data.split('\n')

    def next(self):
        password = self.passwords[self.i]
        self.i += 1
        return password


class GoodPasswordGenerator:
    def __init__(self):
        self.alphabet = '1234567890' \
                        'qwertyuiopasdfghjklzxcvbnm' \
                        'QWERTYUIOPASDFGHJKLZXCVBNM' \
                        '!@#$%^&*()_+'

    def next(self, length=10):
        password = ''
        for i in range(length):
            c = random.choice(self.alphabet)
            password += c
        return password


generator = BadPasswordGenerator()
generator2 = GoodPasswordGenerator()


print(generator.next())
print(generator2.next())

