import os


def save_extension(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split(".")[-1]
            extensions[extension] = extensions.get(extension, []) + [filename]
        elif os.path.isdir(file):
            save_extension(file, first_level=True)


directory = input("Enter the directory name: ")
extensions = {}
result = []

try:
    save_extension(directory)
except FileNotFoundError:
    print("Directory not found")

extensions = sorted(extensions.items(), key=lambda kvp: kvp[0])

for extension, files in extensions:
    result.append(f"{extension}")

    for file in sorted(files):
        result.append(f"- - -{file}")

with open("files/report.txt", "w") as report_file:
    report_file.write('\n'.join(result))
