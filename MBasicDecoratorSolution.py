### 1.1: Basic Decorator
# Create a decorator that adds a greeting to the output of a function.
# When added to another function it will print "Hello!" whenever the decorated function is called upon.

# Decorator
def greet_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorated Geetings to you :) ")
        return func(*args, **kwargs)
    return wrapper

# original function
def say_hello(name):
    return f"Nice to meet you, {name}!"

# Calling the original function - undecorated
print(say_hello("Mehdi! no decoration for you :( "))

# Decorating the original function
@greet_decorator
def say_hello(name):
    return f"Nice to meet you, {name}!"

# Calling the original function - decorated
output = say_hello("Alice")
print(output)