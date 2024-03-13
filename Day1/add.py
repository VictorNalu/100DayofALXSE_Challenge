#!/usr/bin/env python3
"""
A function that adds numbers
"""


def add(*args):
    """Function that add multiple numbers"""

    sum = 0
    for i in args:
        sum += i
    return sum


while True:
    try:
        print("\nHi, there\n")
        numb = input("Enter the numbers you want to add (or type 'q' to quit):\n\n")
        if numb == "q":
            print("\nquitting...")
            break
        num = numb.split()
        num = [int(j) for j in num]
        v = add(*num)
        print(f"\nResult is {v}")
        print(".....................")
    except ValueError:
        print("\n\033[31mPlease enter valid numbers separated by spaces!\033[0m")
        print(".....................")
