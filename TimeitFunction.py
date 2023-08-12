
from timeit import timeit

def normal_impl() -> list[int]:
   return [i for i in (0,1,3,4,4)]

def optmized_impl() ->list[int]:
   return [0,1,2,3,4]


normal_time: float = timeit(stmt=normal_impl)
optimized_time: float = timeit(stmt=optmized_impl)


print(f' Normal implimentation: {round(normal_time, 4)}s',)
print(f' Optimized implimentation: {round(optimized_time, 4)}s',)
