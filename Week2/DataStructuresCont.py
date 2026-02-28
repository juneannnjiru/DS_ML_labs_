# Data structures part 2 
"""
Operators
Arithmetic operators include: + (addition), - (subtraction), * (multiplication), 
/ (division), // (floor division), % (modulo), ** (exponentiation)
"""

# Addition (+)
x = 5
y = 6
print(x + y)

# Subtraction (-)
x = 3
y = 6
print(y - x)

# Multiplication (*)
x = 2
y = 4
print(x * y)

# Division (/)
x = 30
y = 3
print(x / y)

# Floor division (//) - Whole number quotient only. Ignores remainder. 
x = 10
y = 3
print(x // y)

# Modulo (%) - Remainder only. Ignores quotient.
x = 500
y = 6
print(x % y)

# Exponentiation (**)
x = 5
y = 3
print(x ** y)


# Comparison operators (>, <, ==, >=, <=, !=)

# Greater than (>)
x = 64
y = 33
print(x > y)
print(y > x)

# Equal to (==)
x = 42
y = 22
print(x == y)

# Greater than or equal to (>=)
print(x >= y)

# Less than or equal to (<=)
print(x <= y)
print(y <= x)

# Not equal to (!=)
print(x != y)

"""
Logical operators (and, or, not)
And: every statement has to be true. A false statement in a group produces a false result.
Or: if only one condition is true, the outcome will be true.
Not: negation of a statement or condition.
"""
x = 16
y = 23

# And - both conditions must be fulfilled
print(x > y and y > x)

# Or - one, or both conditions are tru
print(x > y or y > x)

# Not
print(not (x < 16))


# Assignment operators - gives variable x a value
x = 65

# Addition assignment - takes value of x and adds the new number
x += 12

# Subtraction assignment
x -= 12

# Multiplication assignment
x *= 12

# Division assignment
x /= 12

# Floor division assignment
x //= 12

# Exponentiation assignment
x **= 12

"""
Bitwise operators
These operators reference integers in 0s and 1s (binary level).
The bitwise operators include: &, |, ^, ~, <<, >>
"""
x = 10
y = 2

# Convert integers to binary - inbuilt function to change value of variablr to binary equivalent
bin(x)
bin(y)

# Bitwise AND (&) Returns a 1 (in binary) only if corresponding bits are ones. Output is in decimal though
print(x & y)

# Bitwise OR (|) returns 1 if one or both corresponding bits are ones
print(x | y)

# Bitwise XOR (^) returns 1 if only one but not both corresponding bits are ones
print(x ^ y)

# Bitwise NOT (~)
print(~x)
print(~y)

"""
Two's complement formula:
~x = -(x + 1)
~y = -(y + 1)
"""
# Right shift (>>)
print(x >> 2)

# Each right shift divides by 2 (floor division for integers)

# Left shift (<<)
print(x << 2)

# Each left shift multiplies by 2

print(x << 5)

"""
Membership operators
These check whether a value exists in a sequence.
The operators are: in, not in
"""

b = (1, 2, 3, 4, 5)

print(4 in b)
print(6 in b)

"""
Identity operators
These check whether two objects share the same memory location.
The operators are: is, is not
"""
a = (1, 2, 3, 4, 5)
b = (1, 2, 3, 4, 5)

print(a == b)
print(a is b)
print(a is not b)

"""
Strings and control flow
Strings are immutable collections of characters used to handle textual data.
Control flow refers to the order in which program statements are executed.
"""

name = "Dangote INC"

# String methods
# Convert to uppercase
print(name.upper())

# Check if alphabetic
print(name.isalpha())

# Convert to lowercase
print(name.lower())

# Check if digit
print(name.isdigit())

# Check if lowercase
print(name.islower())

# Check if uppercase
print(name.isupper())


ballet = "All ballerinas are athletic"

# Split
words = ballet.split(" ")

# Join
print("_".join(words))

# Replace
print(ballet.replace("athletic", "graceful"))

# Startswith
flowers = "Tulips"
print(flowers.startswith("o"))
print(flowers.startswith("T"))

# Endswith
flower = "Peonies"
print(flower.endswith("s"))