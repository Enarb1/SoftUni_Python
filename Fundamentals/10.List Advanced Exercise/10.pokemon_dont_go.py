def sequence_func(sequence):
    sum_removed = 0

    while sequence:
        index_input = int(input())
        if index_input < 0:
            value_rep = sequence[-1]
            sum_removed += sequence[0]
            value = sequence[0]
            sequence[0] = value_rep
        elif index_input >= len(sequence):
            value_rep = sequence[0]
            sum_removed += sequence[-1]
            value = sequence[-1]
            sequence[-1] = value_rep
        else:
            value = sequence[index_input]
            sum_removed += value
            sequence.pop(index_input)

        for index, num in enumerate(sequence):
            if num <= value:
                num += value
                sequence.pop(index)
                sequence.insert(index, num)
            elif num > value:
                num -= value
                sequence.pop(index)
                sequence.insert(index, num)
    return sum_removed


sequence = list(map(int, input().split()))
result = sequence_func(sequence)
print(result)

