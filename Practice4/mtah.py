import math
import random


def square_root(x):
    return math.sqrt(x)


def factorial(n):
    return math.factorial(n)


def random_number(start, end):
    return random.randint(start, end)


def circle_area(radius):
    return math.pi * radius ** 2


if __name__ == "__main__":
    print(square_root(16))
    print(factorial(5))
    print(random_number(1, 10))
    print(circle_area(5))