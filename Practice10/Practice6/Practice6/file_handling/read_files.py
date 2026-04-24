# Example 1: Read entire file
with open("sample.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)

# Example 2: Read line by line
with open("sample.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())

# Example 3: Read all lines into a list
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("All lines:", lines)