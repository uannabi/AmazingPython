from typing import Union
from functools import singledispatch

@singledispatch
def func(arg):
   print(f'Default: {arg}')

@func.register
def _(arg: int | float): #python3.10
#def _(arg: Union[int, float]): 
   print(f'Number: {arg}')

@func.register
def _(arg: str):
   print(f'String: {arg}')

func(None)
func(19.5)
func('Hello')

