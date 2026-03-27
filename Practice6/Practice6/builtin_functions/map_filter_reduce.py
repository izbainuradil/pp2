from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Example 1: Map (square all numbers)
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

# Example 2: Filter (even numbers only)
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# Example 3: Reduce (sum of all numbers)
total = reduce(lambda a, b: a + b, numbers)
print("Sum:", total)