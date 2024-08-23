line = input().split("|")

sub_lists = []

for sub_string in line[::-1]:
    sub_lists.extend(sub_string.split())

print(*sub_lists)
"""Solution 2"""
# numbers = [string.split() for string in input().split("|")]
# print(*[' '.join(sublist) for sublist in numbers[::-1] if sublist])