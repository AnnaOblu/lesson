def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
    return wrapper

def get_memory(f):
    import sys
    def wrapper(*args, **kwargs):
        print(f(*args, **kwargs))
        print('Объем занимаемой памяти: ', sys.getsizeof(f))
    return wrapper

@get_memory
@benchmark
def my_list():
   simple_list = [x+1 for x in range(100000)]
   for i in simple_list:
      print('Список')
      return simple_list

my_list()

@get_memory
@benchmark
def my_gen(num):
    simple_generator = (x+1 for x in range(num))
    print('Генератор')
    return simple_generator


my_gen(100000)


