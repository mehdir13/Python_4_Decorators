### 1.3 Repeating Decorator
# Write a decorator that takes in the argument n. The decorated function should be run n times.

#prompt user to enter a valid number of repetitions:
def get_valid_n_repetition():
    while True:
        try:
            n = int(input("Enter the number of repetitions (an integer > 1): "))
            if n > 1:
                return n
            else:
                print(" <<  Please enter an integer greater than 1  0>>")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

n = get_valid_n_repetition()

def n_time_repeater_function(n):
    def repeator_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        #    return result
        return wrapper
    return repeator_decorator

@n_time_repeater_function(n)
def function():
    print("Bart Simpson should write this many times!")

function()

# OPTIONAL: user can enter the number of times of repetition. the firs function, before the decorator, prompts user to enter a valid input.
# BONUS: we used a "try... except" block :)
# "def n_time_repeater_function(n)": Parameterized Decorators (a Decorator With Arguments).
# The underscore _ is used as variable name to indicate that the value of the variable is insignificant or irrelevant.
# "return repeator_decorator": this line allows the outer function to return the inner decorator function.
# Needless to say: "return wrapper": The inner decorator returns wrapper, which contains the logic for executing the original function multiple times based on the argument.
# However, a parameterized decorator needs both return wrapper [just like a simple decorator] besides a return decorator line to return the decorator that can accept the original function.
# We could rewrite the wrapper as follow, if we had a outer function which could return a value that we wantet ot pass on.

#  def wrapper(*args, **kwargs):
#            for _ in range(n):
#                result = func(*args, **kwargs)
#            return result
#        return wrapper
