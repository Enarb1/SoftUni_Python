n, m = input().split()

first_set = {int(input()) for num in range(int(n))}
second_set = {int(input()) for numb in range(int(m))}

final = first_set.intersection(second_set)
print(*final, sep='\n')
