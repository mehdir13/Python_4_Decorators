# Took the Is Prime function ecorated it by the timer decorater and tested the running time for primes numbers in the Fibonacci sequence.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time is: {execution_time:.4f} seconds")
        return result
    return wrapper

@timer
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


print(is_prime(10**7 + 1))
print(is_prime(10**7 + 5))
print(is_prime(2971215073))
print(is_prime(99194853094755497))              # 12.50 seconds

#print(is_prime(1066340417491710595814572169))  # TOO BIG FOR MY LAPTOP Over 2 minutes and I stopped the program manually before printing the result
#print(is_prime(19134702400093278081449423917)) # TOO BIG FOR MY LAPTOP
