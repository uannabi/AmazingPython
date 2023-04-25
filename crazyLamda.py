
x = lambda a:print(a)
x('normal')

y = lambda a: lambda b: print(a, b)
y('a')('b')
