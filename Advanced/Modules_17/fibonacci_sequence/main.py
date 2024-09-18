from Advanced.Modules_17.fibonacci_sequence.core import fibonacci, locate_num

command = input()
seq = None
while command != "Stop":
    if command.startswith("Create"):
        data = command.split()
        number = int(data[-1])
        seq = fibonacci(number)
        print(seq)
    elif command.startswith("Locate"):
        data = command.split()
        number_to_locate = int(data[-1])
        if seq:
            index = locate_num(seq, number_to_locate)
            print(f"The number - {number_to_locate} is at index {index}") if isinstance(index, int) \
                else print(locate_num(seq, number_to_locate))
        else:
            print("Firs create a sequence")
    command = input()




