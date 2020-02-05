from lesson_5 import prime_num, factor, divider


def test_prime_num():
    y = prime_num(41)
    if y > 0:
        print('Тест ОК')
    else:
        print('Ошибка')

print(test_prime_num())


def test_divider():
    y = divider(60)
    if y % 2 == 0:
        print('Тест не пройден. Число непростое')
    else:
        print('Тест Oк')

print(test_divider())


def test_prime_num_2():
    assert prime_num(17) == True


def test_factor():
    assert factor(455) == [5, 7, 13]


def test_divider_2():
    assert divider(230) == 23
