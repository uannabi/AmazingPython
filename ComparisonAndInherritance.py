"""
In this example, we define a Person class with an __init__ method that takes a name and age argument, and overrides the __eq__ and __ne__ methods to compare Person objects based on their name and age attributes.

We then define an Employee class that inherits from the Person class and adds an id attribute.

We create two Person objects with the same name and age, and compare them using the == operator, which calls the __eq__ method. The comparison returns True, indicating that the two objects are equal.

We then create two Employee objects with the same name, age, and id, and compare them using the == operator, which also calls the __eq__ method inherited from the Person class. The comparison returns True, indicating that the two objects are equal.

This example demonstrates how comparison operators can be customized in a class, and how inheritance allows child classes to inherit and extend the behavior of their parent class.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

# Create two Person objects with the same name and age
person1 = Person("John", 30)
person2 = Person("John", 30)

# Compare the two Person objects
print(person1 == person2)  # Output: True

# Create two Employee objects with the same name, age, and ID
employee1 = Employee("Jane", 25, 123)
employee2 = Employee("Jane", 25, 123)

# Compare the two Employee objects
print(employee1 == employee2)  # Output: True

