
groups= [[1,2], [5,6]]

for g in groups:
   for elem in g:
      print(elem, end='')

c = [elem for g in groups for elem in g]

print(c)
