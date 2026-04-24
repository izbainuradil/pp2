names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Example 1: Enumerate
for index, name in enumerate(names):
    print(f"{index}: {name}")

# Example 2: Zip two lists
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Example 3: Type conversion
str_numbers = ["1", "2", "3"]
int_numbers = list(map(int, str_numbers))
print("Converted to int:", int_numbers)