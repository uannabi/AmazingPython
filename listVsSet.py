
from timeit import timeit

my_list = list(range(100_000))
my_set  = set(range(100_00))


list_time = timeit(stmt = '99_999 in my_list', number=1000, globals=globals())
print(f'list:{list_time:.6f} seconds')

set_time = timeit(stmt = '99_999 in my_set', number=1000, globals=globals())

print(f'set:{set_time:.6f} seconds')
