# Example 1: Write to a file (overwrite)
with open("output.txt", "w") as f:
    f.write("Hello, Python!\n")
    f.write("File handling example.\n")

# Example 2: Append to a file
with open("output.txt", "a") as f:
    f.write("Appending a new line.\n")

# Example 3: Using context manager with a list
lines = ["First line\n", "Second line\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)