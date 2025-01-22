def show_args_kwargs(*args, **kwargs):
    print("Positional arguments (*args):")
    for i, arg in enumerate(args, start=1):
        print(f"  Argument {i}: {arg}")
        
    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

# Example usage:
show_args_kwargs(1, 2, 3, name="Alice", age=30, location="Wonderland")



# Step 1: Assigning a function to a variable
def greet():
    return "Hello!"

say_hello = greet  # Assign the function to a variable
print("Step 1 - Function as variable:", say_hello())  # Output: Hello!


# Step 2: Creating a decorator manually (without @ syntax)
def shout(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

greet = shout(greet)  # Manually decorate the function
print("Step 2 - Manual decorator (no @):", greet())  # Output: HELLO!


# Step 3: Using a decorator with @ syntax (no arguments)
@shout
def excited_greet():
    return "Hello!"

print("Step 3 - Decorator with @ syntax:", excited_greet())  # Output: HELLO!


# Step 4: Creating a decorator with arguments
def exclaim(times):
    def decorator(func):
        def wrapper():
            original_result = func()
            modified_result = original_result + "!" * times
            return modified_result
        return wrapper
    return decorator

# Without @ syntax
def simple_greet():
    return "Hello"

simple_greet = exclaim(3)(simple_greet)  # Manually apply the decorator with arguments
print("Step 4 - Decorator with arguments (no @):", simple_greet())  # Output: Hello!!!

# With @ syntax
@exclaim(5)
def enthusiastic_greet():
    return "Hello"

print("Step 4 - Decorator with arguments and @ syntax:", enthusiastic_greet())  # Output: Hello!!!!!


# Example usage
def requires_permission(permission):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if permission in user.get('permissions', []):
                return func(user, *args, **kwargs)
            else:
                print(f"User lacks {permission} permission")
        return wrapper
    return decorator

@requires_permission('admin')
def delete_data(user):
    print("Data deleted")

user = {'name': 'Alice', 'permissions': ['user']}
delete_data(user)  # Output: User lacks admin permission
