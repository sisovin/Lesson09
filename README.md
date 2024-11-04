# Lesson 09: Functions

## What are functions in Python?

/\*\*

- Functions in Python are blocks of reusable code that perform a specific
- task. They help in organizing code, making it more readable, and reducing
- redundancy. Here's a brief overview:
  \*\*/

1. **Definition**: Functions are defined using the `def` keyword followed by the function name and parentheses `()`.

2. **Parameters**: Functions can take parameters (arguments) which allow you to pass data into them.

3. **Return Value**: Functions can return a value using the `return` statement.

4. **Calling a Function**: You call a function by using its name followed by parentheses.

### Example

```python
# Define a function
def greet(name):
    return f"Hello, {name}!"

# Call the function
message = greet("Alice")
print(message)  # Output: Hello, Alice!
```

### Key Points

- **Modularity**: Functions allow you to break down complex problems into smaller, manageable pieces.
- **Reusability**: Once a function is defined, it can be reused multiple times throughout your code.
- **Abstraction**: Functions help in hiding the implementation details and expose only the necessary parts.

Functions are fundamental in Python and are used extensively in both simple scripts and complex applications.

## Passing multiple arguments to functions

To pass multiple arguments to a Python function, you simply list them within the parentheses when defining the function. When calling the function, you provide the corresponding values in the same order.

### Example

```python
# Define a function with multiple arguments
def add_numbers(a, b):
    return a + b

# Call the function with multiple arguments
result = add_numbers(5, 3)
print(result)  # Output: 8
```

### Key Points

- **Order Matters**: The order of arguments in the function call must match the order of parameters in the function definition.
- **Positional Arguments**: The arguments are passed based on their position.
- **Keyword Arguments**: You can also pass arguments using the parameter names, which allows you to change the order.

### Example with Keyword Arguments

```python
# Define a function with multiple arguments
def greet(first_name, last_name):
    return f"Hello, {first_name} {last_name}!"

# Call the function with keyword arguments
message = greet(last_name="Doe", first_name="John")
print(message)  # Output: Hello, John Doe!
```

### Variable-Length Arguments

Python also allows you to pass a variable number of arguments using `*args` and `**kwargs`.

#### Example with `*args`

```python
# Define a function with variable-length positional arguments
def sum_all(*args):
    return sum(args)

# Call the function with multiple arguments
result = sum_all(1, 2, 3, 4)
print(result)  # Output: 10
```

#### Example with `**kwargs`

```python
# Define a function with variable-length keyword arguments
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with multiple keyword arguments
print_details(name="Alice", age=30, city="Wonderland")
# Output:
# name: Alice
# age: 30
# city: Wonderland
```

These techniques provide flexibility in how you pass data to functions in Python.

### Using both positional and keyword arguments

You can pass arguments to a Python function using both positional and keyword arguments by specifying the positional arguments first, followed by the keyword arguments. This allows you to mix and match how you pass data to the function.

### Example

```python
# Define a function with multiple parameters
def describe_pet(pet_name, animal_type="dog", age=None):
    description = f"I have a {animal_type} named {pet_name}."
    if age:
        description += f" {pet_name} is {age} years old."
    return description

# Call the function using both positional and keyword arguments
description1 = describe_pet("Willie")
print(description1)  # Output: I have a dog named Willie.

description2 = describe_pet("Harry", "hamster")
print(description2)  # Output: I have a hamster named Harry.

description3 = describe_pet("Bella", age=5)
print(description3)  # Output: I have a dog named Bella. Bella is 5 years old.

description4 = describe_pet("Max", "cat", age=3)
print(description4)  # Output: I have a cat named Max. Max is 3 years old.
```

### Key Points

- **Positional Arguments**: These are passed first and are matched based on their position.
- **Keyword Arguments**: These are passed after positional arguments and are matched based on the parameter names.
- **Flexibility**: This approach provides flexibility in how you call the function, allowing you to specify only the necessary arguments and use defaults for others.

Using both positional and keyword arguments can make your function calls more readable and flexible.

## Defining default values for function parameters

In Python, you can define default values for function parameters by assigning a value to the parameter in the function definition. If an argument for that parameter is not provided when the function is called, the default value will be used.

### Example

```python
# Define a function with default parameter values
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Call the function without the default parameter
message1 = greet("Alice")
print(message1)  # Output: Hello, Alice!

# Call the function with the default parameter
message2 = greet("Bob", "Hi")
print(message2)  # Output: Hi, Bob!
```

### Key Points

- **Default Parameters**: Default values are specified in the function definition.
- **Optional Arguments**: Parameters with default values become optional when calling the function.
- **Order**: Parameters with default values must come after parameters without default values in the function definition.

### Example with Multiple Default Values

```python
# Define a function with multiple default parameter values
def describe_pet(pet_name, animal_type="dog"):
    return f"I have a {animal_type} named {pet_name}."

# Call the function with only the required argument
description1 = describe_pet("Willie")
print(description1)  # Output: I have a dog named Willie.

# Call the function with both arguments
description2 = describe_pet("Harry", "hamster")
print(description2)  # Output: I have a hamster named Harry.
```

Using default values for function parameters can make your functions more flexible and easier to use.

The code you provided should correctly sum the arguments and display `10`. If the result is displaying `0`, there might be an issue elsewhere in your code or environment. However, let's review the code to ensure everything is correct.

### Code Review

```python
# Define a function with variable-length positional arguments
def sum_all(*args):
    return sum(args)

# Call the function with multiple arguments
result = sum_all(1, 2, 3, 4)
print(result)  # Expected output: 10
```

### Explanation

1. **Function Definition**: The `sum_all` function takes a variable number of positional arguments using `*args`.
2. **Summing Arguments**: The `sum` function is used to sum all the arguments passed to `sum_all`.
3. **Function Call**: The function is called with the arguments `1, 2, 3, 4`, which should sum to `10`.
4. **Print Result**: The result is printed, which should be `10`.

### Possible Issues

- **Environment Issue**: Ensure that there are no other definitions of `sum_all` in your environment that might be causing the issue.
- **Code Execution**: Make sure you are running the correct version of the script.

### Debugging Steps

1. **Print Arguments**: Add a print statement inside the function to verify the arguments.
2. **Check for Other Definitions**: Ensure there are no other conflicting definitions of `sum_all`.

### Updated Code with Debugging

```python
# Define a function with variable-length positional arguments
def sum_all(*args):
    print(f"Arguments received: {args}")  # Debugging statement
    return sum(args)

# Call the function with multiple arguments
result = sum_all(1, 2, 3, 4)
print(result)  # Expected output: 10
```

Run this updated code to see the debug output and verify that the arguments are being passed correctly. If the issue persists, check your environment for any conflicts or errors.
