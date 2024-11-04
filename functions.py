# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %%
from turtle import title


print("")
title = " Functions ".upper()
print(f"{title:*^50}")
# Functions
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
def hello_world():
    print("Hello, World!")

hello_world()
# %%
def sum(num1=0, num2=0):
    if (type(num1) is not int) or (type(num2) is not int):
        return 0
    return num1 + num2
  
total = sum(10, 5)
print(total)
# %%
def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Sisovin", "Sovanny", "Vuddhi")
# %%
def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

multi_named_items(first="Sisovin", last="Chieng", age=52, country="Cambodia")
# %%
# Define a function
def greet(name):
    return f"Hello, {name}!"

# Call the function
message = greet("Sisovin")
print(message)  # Output: Hello, Sisovin!
# %%
# Define a function with multiple arguments
def add_numbers(a, b):
    return a + b

# Call the function with multiple arguments
result = add_numbers(5, 3)
print("Output =", result)  # Output: 8
# %%
# Define a function with multiple arguments with the alert message to the console
def greet(first_name, last_name):
    return f"Hello, {first_name} {last_name}!"

def alert(message):
    return f"Alert: {message}"

# Call the function with keyword arguments
message = greet(last_name="Doe", first_name="John")
print(alert(message))
# %%
# Define a function with variable-length positional arguments
def sum_all(*args):
    print(f"Arguments received: {args}")  # Debugging statement
    return sum(args)

# Call the function with multiple arguments
result = sum_all(1, 2, 3, 4)
print(result)  # Expected output: 10  
print("")
# %%
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
# %%
# Define a function with default parameter values
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Call the function without the default parameter
message1 = greet("Alice")
print(message1)  # Output: Hello, Alice!

# Call the function with the default parameter
message2 = greet("Bob", "Hi")
print(message2)  # Output: Hi, Bob!
# %%
# Define a function with multiple default parameter values
def describe_pet(pet_name, animal_type="dog"):
    return f"I have a {animal_type} named {pet_name}."

# Call the function with only the required argument
description1 = describe_pet("Willie")
print(description1)  # Output: I have a dog named Willie.

# Call the function with both arguments
description2 = describe_pet("Harry", "hamster")
print(description2)  # Output: I have a hamster named Harry.
# %%
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

