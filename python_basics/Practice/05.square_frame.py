n = int(input())

print("+"+" -" * (n - 2) + " +")

for _ in range(n - 2):
    print("|" + " -" * (n - 2) + " |")

print("+" + " -" * (n - 2) + " +")



