#!/usr/bin/python3
"""Print the numbers from1 to 100 separated by a space.
For multiples of three, print Fizz instead of the number
For multiples of five, print Buzz instead of the number.
For multiples of three and five, print Fizzbuzz instead of the number.
"""


def fizzbuzz():
    for number in range(1, 101):
        if numer % 3 == 0 and number % 5 == 0:
            print("Fizzbuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ". format(number), end="")
