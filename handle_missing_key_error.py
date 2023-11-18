class CustomDict(dict):
   def __missing__(self, key):
      return f'key: "{key}" does not exist'


data = {'a':1, 'b':2, 'c':3,'d':4}
cd = CustomDict(data)

print(cd['A'])
print(cd)
