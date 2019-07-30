"""
Calculator

Write a simple calculator that reads the three input lines: the first number, the second number and the operation, after which it applies the operation to the entered numbers ("first number" "operation" "second number") and outputs the result to the screen. Note that the numbers can be real.

Supported operations: +, -, /, *, mod, pow, div; where
mod — taking the residue,
pow — exponentiation,
div — integer division.

If a user performs the division and the second number is 0, it is necessary to output the line "Division by 0!".
"""

args = [float(i) if '.' in i else int(i) for i in [input(), input()]]

try:
    print({
              'mod': lambda x, y: x % y,
              'pow': lambda x, y: x**y,
              'div': lambda x, y: x // y,
              '+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '/': lambda x, y: x / y,
              '*': lambda x, y: x * y,
          }[input()](*args))
except ZeroDivisionError:
    print("Division by 0!")
