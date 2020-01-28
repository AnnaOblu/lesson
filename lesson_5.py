# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами)

def prime_num(n):
    x = 2
    while n % x != 0:
        x += 1
    return x == n

print(prime_num(34))


# 2) выводит список всех делителей числа;
def factor(n):
    result = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            result.append(i)
        else:
            i += 1
    if n > 1:
        result.append(n)
    return result


print(factor(78))


# 3) выводит самый большой простой делитель числа

def divider(a):
    prime_num = factor(a)
    max_num = 0
    for i in prime_num:
        if i > max_num:
            max_num = i
    return (max_num)


print(divider(154))
