import math

value1 = float('nan')
print(f'this value is number{ math.isnan(value1)}')
value2 = float('inf')
#print(math.isnan(value2))
print(f'this value is number{ math.isinf(value2)}')
value3 = float('-inf')
print(f'this value is number{ math.isinf(value3)}')
