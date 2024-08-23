loop_range = int(input())
my_stack = []

for _ in range(loop_range):
    command = input().split()
    if command[0] == '1':
        num = int(command[1])
        my_stack.append(num)
    elif my_stack:
        if command[0] == '2':
            my_stack.pop()
        elif command[0] == '3':
            print(max(my_stack))
        elif command[0] == '4':
            print(min(my_stack))
print(", ".join([str(x) for x in reversed(my_stack)]))
