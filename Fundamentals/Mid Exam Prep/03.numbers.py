def sorted_list(integer_input):
    average_num = sum(num for num in integer_input) / len(integer_input)
    top_five = [num for num in integer_input if num > average_num]

    if len(top_five) == 0:
        return "No"
    elif len(top_five) <= 5:
        result = sorted(top_five, reverse=True)
        return " ".join(map(str,result))
    elif len(top_five) > 5:
        top_five = sorted(top_five,reverse=True)
        result = top_five[:5]
        return " ".join(map(str,result))


int_input = list(map(int, input().split()))

print(sorted_list(int_input))
