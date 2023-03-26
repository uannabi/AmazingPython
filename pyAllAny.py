
list =[-1,1,0,2]
if any(n>0 for n in list):
   print('success')

if all(n>0 for n in list):
   print('success')
