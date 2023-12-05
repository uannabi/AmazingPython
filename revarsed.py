
class Backwards(list):
   def __reversed__(self):
      return self[::-1]

bs = Backwards([1,2,3,4,5])
print(f'original:{bs}')

print(f'Reversed{reversed(bs)}')
