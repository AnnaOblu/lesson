import string
from collections import Counter
x_srt = open('text.txt', 'r', encoding='UTF-8')
x_srt = x_srt.read()
print(x_srt)

# задание 1 методами строк очистить текст от знаков препинания

'''
import re

x_srt = input('Введите текст ')
x_srt = x_srt.replace('-', ' ') #мы заменяем(re.sub) все NON[буквенно-цифровые символы(\w) и пробелы(\s)] пустой строкой.
x_srt = re.sub(r'[^\w\s]','',x_srt)

print(x_srt)
'''

x_srt = x_srt.replace('-', ' ')
x_srt = x_srt.translate(str.maketrans('', '', string.punctuation))
print(x_srt)

# задание 2 сформировать list со словами (split)

x_list = x_srt.split()
print(x_list)

# задание 3 привести все слова к нижнему регистру (map)

new_list = list(map(lambda x:x.lower(), x_list))
print(new_list)

# задание 4 получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;

x_dict = {}
for i in range(len(new_list)):
    x_dict[new_list[i]] = new_list.count(new_list[i])
print(x_dict)

# задание 5 вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).

y_dict = Counter(x_dict).most_common(5)

print(y_dict)