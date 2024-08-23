number = int(input())
is_Prime = True

for index in range(2, number):
    if number % index == 0:
        is_Prime = False
print(is_Prime)