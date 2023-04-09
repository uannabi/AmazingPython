
box =[[1,3,5],[2,4,6],[7,8,9]]

for item in box:
   for things in item:
      print(things)
nex_box=[]
new_box = [i for j in box for i in j]

print(nex_box)

from itertools import chain

chained = list(chain(*box))
print(chained)
