from random import choices
from collections import Counter


#1. Напишите функцию (F): на вход список имен и целое число N;
#на выходе список длины N случайных имен из первого списка (могут повторяться, можно взять значения:
#количество имен 20, N = 100, рекомендуется использовать функцию random);

name_list = ['Alexandra', 'Bella', 'Violleta', 'Gabriella', 'Cornelius', 'Stephany', 'Oliver',
             'Robert', 'Feliciti', 'Chloe', 'Charlotte', 'Tara', 'Steven', 'Mia', 'Ophelia', 'John',
             'Isabella', 'Ethan', 'Elaine', 'Jennifer']


def choice_name(names, len_list):
    """функция принимает список имён и длину списка,
    возвращает случайный элемент из списка заданное кол-во раз"""

    return choices(names, k=len_list)


new_list = choice_name(name_list, 100)
print(new_list)

# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;

name_dict = {}
for i in range(len(new_list)):
    name_dict[new_list[i]] = new_list.count(new_list[i])

often_name = Counter(name_dict).most_common(1)

print(often_name)

# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.


letters = []
for word in name_list:
    letters+= word[0]

letters_dict = {}

for let in letters:
    letters_dict[let] = letters.count(let)

print(list(letters_dict)[-1])
