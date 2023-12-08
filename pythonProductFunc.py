
from itertools import product 

colors = ['Red', 'Black', 'Green']
sizes = [1947, 1964, 1986, 2008, 2123]

combinations = product(colors, sizes)


for item in combinations: 
   print(item)
