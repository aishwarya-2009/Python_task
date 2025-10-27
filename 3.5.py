# main.py
from math_string_operations.math_operations import add, multiply, factorial
from math_string_operations.string_operations import reverse_string, count_vowels

# Mathematical Operations
print("Mathematical Operations:")
print(f"Addition of 5 and 3: {add(5, 3)}")
print(f"Multiplication of 5 and 3: {multiply(5, 3)}")
print(f"Factorial of 5: {factorial(5)}")

# String Operations
print("\nString Operations:")
sample_string = "Hello World"
print(f"Reverse of '{sample_string}': {reverse_string(sample_string)}")
print(f"Number of vowels in '{sample_string}': {count_vowels(sample_string)}")
