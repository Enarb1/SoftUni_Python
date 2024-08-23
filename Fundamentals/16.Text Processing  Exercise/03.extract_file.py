file_path = input().split("\\")
file = file_path[-1].split('.')
print(f'File name: {file[0]}\nFile extension: {file[1]}')
