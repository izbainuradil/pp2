import shutil
import os

# Example 1: Copy a file
shutil.copy("output.txt", "backup_output.txt")

# Example 2: Move a file
os.makedirs("directory_backup", exist_ok=True)
shutil.move("backup_output.txt", "directory_backup/backup_output.txt")

# Example 3: Delete a file safely
if os.path.exists("output.txt"):
    os.remove("output.txt")
    print("File deleted")
else:
    print("File not found")