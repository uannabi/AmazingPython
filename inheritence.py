"""
In this example, we define an Animal class with an __init__ method that takes a name and sound argument, and a make_sound method that prints the animal's name and sound.

We then define a Dog class and a Cat class that both inherit from the Animal class using the super() function. The Dog and Cat classes each have an __init__ method that calls the Animal class's __init__ method with a default sound of "bark" or "meow", respectively.

We create instances of the Dog and Cat classes and call the make_sound method on each instance, which prints the animal's name and sound.

This is a simple example of inheritance, but it demonstrates how child classes can inherit attributes and methods from their parent class, and how child classes can extend or modify the behavior of their parent class.
"""
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.name} says {self.sound}")
        
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "bark")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "meow")

# Create instances of the Dog and Cat classes
my_dog = Dog("Fido")
my_cat = Cat("Fluffy")

# Call the make_sound method on the Dog and Cat instances
my_dog.make_sound()  # Output: Fido says bark
my_cat.make_sound()  # Output: Fluffy says meow

