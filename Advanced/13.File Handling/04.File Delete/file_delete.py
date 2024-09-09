import os

path = os.path.join("..", "03.File Writer", "my_first_file.txt")

if os.path.exists(path):
    os.remove(path)
else:
    print("File already deleted!")