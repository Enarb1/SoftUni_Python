number = int(input())
num = 1

for row in range(1, number + 1 ):
    for column in range(row):
        if num <= number:
            print(num,end=" ")
            num += 1
    print(" ")