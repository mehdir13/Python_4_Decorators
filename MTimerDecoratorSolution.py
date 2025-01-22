### 1.2: Timer Decorator
# Create a decorator that measures the execution time of a function.
# 1. Create a decorator named `timer` that prints the time it takes for a function to execute.
# 2. Apply this decorator to a function `slow_function()` that simulates a delay (e.g., using `time.sleep()`) before returning a value.
# 3. Call `slow_function()` and observe the output.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the starting time of the original function
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the ending time of the original function
        execution_time = end_time - start_time
        print(f"Execution time is: {execution_time:.4f} seconds")
        return result  # Return the original function's result
    return wrapper

# a slow function
@timer
def slow_function():
    time.sleep(2)  # Simulate a delay of 2 seconds
    return "Function completed!"

# Call the decorated function
print("Function starts ...")
output = slow_function()
print(output)


@timer
def is_prime(n):
    if n <= 1:
        return False  # 0, 1, and negative numbers are not prime
    if n <= 3:
        return True   # 2 and 3 are prime numbers
    if n % 2 == 0 or n % 3 == 0:
        return False  # Multiple of 2 or 3 are not prime

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


print(is_prime(10**7 + 1))
print(is_prime(10**7 + 5))
#print(is_prime(2971215073))
#print(is_prime(99194853094755497))

 #assert is_prime(1066340417491710595814572169) == True    # TOO BIG FOR MY LAPTOP
 #assert is_prime(19134702400093278081449423917) == True   # TOO BIG FOR MY LAPTOP
