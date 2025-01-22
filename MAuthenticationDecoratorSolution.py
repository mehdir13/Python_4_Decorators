### 1.4 Authentication Decorator
# Write a decorator that will act as a very basic authentication.
# If the decorated function is called with `password="123"`  the function will run as normally,
# otherwise `{msg: "Not authenticated"}` should be returned.


def authenticate(func):
    def wrapper(*args, **kwargs):
        # Prompt the user for the password
        user_password = input("Enter the password: ")
        # The correct password is hardcoded as "123"
        if user_password == "123":
            return func(*args, **kwargs)  # Call the original function if authenticated
        else:
            return {"msg": "Not authenticated"}  # Return a message if authentication fails
    return wrapper  # Return the wrapper function

@authenticate  # Use the authentication decorator
def sensitive_function(data):
    return f"Sensitive data: {data}"

# Testing the function
response = sensitive_function(data="Here is some confidential information")
print(response)  # Output will depend on the user's password input
