### 1.1: Basic Decorator

Create a decorator that adds a greeting to the output of a function. When added to another function it will print "Hello!" whenever the decorated function is called upon.

---

## Harder exercises

### 1.2: Timer Decorator

Create a decorator that measures the execution time of a function.

1. Create a decorator named `timer` that prints the time it takes for a function to execute.
2. Apply this decorator to a function `slow_function()` that simulates a delay (e.g., using `time.sleep()`) before returning a value.
3. Call `slow_function()` and observe the output.

**Example Output**:

```
slow_function took X.XXX seconds
```

---

### 1.3 Repeating Decorator
Write a decorator that takes in the argument n. The decorated function should be run n times.

### 1.4 Authentication Decorator
Write a decorator that will act as a very basic authentication. If the decorated function is called with `password="123"`  the function will run as normally, otherwise `{msg: "Not authenticated"}` should be returned.
