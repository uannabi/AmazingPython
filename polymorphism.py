
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Create instances of different shapes
rectangle = Rectangle(5, 3)
circle = Circle(4)

# Call area and perimeter methods on different shapes
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

"""
In the example above, we have a base class Shape that defines two methods: area() and perimeter(). This class acts as a common interface for different shapes.

We then create two subclasses, Rectangle and Circle, that inherit from the Shape class. Each subclass overrides the area() and perimeter() methods according to its specific implementation.

By utilizing polymorphism, we can create instances of different shapes (Rectangle and Circle) and treat them as instances of the base class (Shape). This allows us to call the area() and perimeter() methods on these objects without worrying about their specific implementations.

When we call rectangle.area() or circle.area(), the appropriate area() method for each shape is invoked based on the object's type. Similarly, when we call rectangle.perimeter() or circle.perimeter(), the corresponding perimeter() method is called.

Polymorphism enables us to write more flexible and reusable code by providing a common interface that can be implemented differently by different classes.

"""
