hunderts = int(input())
tens = int(input())
ones = int(input())

for n1 in range(1, hunderts + 1):
    if n1 % 2 == 0:
        for n2 in range(2, tens + 1):
            is_prime = True
            for i in range(2, n2):
                if n2 % i == 0:
                    is_prime = False
                    break
            if is_prime and n2 < 8:
                for n3 in range(1, ones + 1):
                    if n3 % 2 == 0:
                        print(f"{n1} {n2} {n3}")


