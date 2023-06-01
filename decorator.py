
def decorator_function(original_function):
    def wrapper_function():
        print("Before the function is called")
        original_function()
        print("After the function is called")
    return wrapper_function

@decorator_function
def greet():
    print("Hello, world!")

# Calling the decorated function
greet()



