
from dataclasses import dataclass 

@dataclass
class Fruit:
   name: str
   cost: float


banana = Fruit('Banana',10)
apple = Fruit('Apple',5)

print(banana)
print(banana == apple)
