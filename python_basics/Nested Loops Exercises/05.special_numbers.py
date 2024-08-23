N = int(input())

for i in range(1111,9999):
    string_n = str(i)
    total_4 = 0
    for j in string_n:
        if int(j) != 0:
            if N % int(j) == 0:
                total_4 += 1
            if total_4 == 4:
                print(i, end=" ")

