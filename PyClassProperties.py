
class Car:
    def __init__(self, brand: str):
        self.brand = brand

    def __str__(self) -> str:
        return f'Car: {self.brand}'

    def __repr__(self)-> str:
        return object.repr(self)


car = Car('Mini')

print(car)
