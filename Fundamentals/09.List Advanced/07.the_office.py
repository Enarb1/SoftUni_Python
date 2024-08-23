def employee_happiness(happiness_lst, factor):

    improved_lst = [factor * current_value for current_value in happiness_lst]
    average_happiness = sum(improved_lst) / len(improved_lst)
    happy_count = sum(num >= average_happiness for num in improved_lst)
    total_count = len(improved_lst)

    message = 'happy' if happy_count >= total_count / 2 else 'not happy'

    return f"Score: {happy_count}/{total_count}. Employees are {message}!"


happiness_list = list(map(int, input().split()))
improvement_factor = int(input())

print(employee_happiness(happiness_list, improvement_factor))