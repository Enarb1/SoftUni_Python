number_of_lines = int(input())
positive_list = []
negative_list =[]


for number in range(number_of_lines):
    current_number = int(input())
    if current_number >= 0:
        positive_list.append(current_number)
    elif current_number < 0:
        negative_list.append(current_number)
print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}\nSum of negatives: {sum(negative_list)}")

