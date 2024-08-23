range_a = int(input())
range_b = int(input())
passwords = int(input())

A = ord("#")
B = ord("@")
pass_counter = 0

for x in range(1, range_a + 1):
    for y in range(1, range_b + 1):
        print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
        A += 1
        B += 1
        pass_counter += 1
        if pass_counter >= passwords:
            exit()
        if A > ord("7"):
            A = ord("#")
        if B > ord("`"):
            B = ord("@")




