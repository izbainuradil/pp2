import shutil
import os

# Example 1: Move a file to another directory
os.makedirs("destination", exist_ok=True)
shutil.move("example.txt", "destination/example.txt")

# Example 2: Copy a file
shutil.copy("destination/example.txt", "destination/example_copy.txt")

# Example 3: Find all .txt files in a directory
txt_files = [f for f in os.listdir("destination") if f.endswith(".txt")]
print("Text files:", txt_files)