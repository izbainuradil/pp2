import os

# Example 1: Create nested directories
os.makedirs("dir1/dir2/dir3", exist_ok=True)

# Example 2: List all files and folders in current directory
print("Directory contents:", os.listdir("."))

# Example 3: Change current working directory
os.chdir("dir1/dir2")
print("Current directory:", os.getcwd())