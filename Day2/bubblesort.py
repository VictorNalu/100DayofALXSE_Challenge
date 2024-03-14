#!/usr/bin/ env python3
"""A function that bubble sorts a list of numbers"""


def bubblesort(a):
    """sorts through a list of numbers in ascending order"""
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                print("\nsorting...\n")
                print(a)
    return a


try:
    user_input = input("\nEnter the numbers you want to sort:\n\n")
    v = [int(c) for c in user_input.split()]
    print(f"\n{v}")
    b = bubblesort(v)
    print("\nFinished sorting.")
    print(f"\nYour sorted numbers:{b}\n")
except ValueError:
    print("\n\033[31mError: Please enter only valid numbers!\033[0m\n")
