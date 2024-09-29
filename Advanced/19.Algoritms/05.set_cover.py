def set_cover(universe, sets_input):
    chosen_sets = []

    while universe:
        best_set = max(sets_input, key=lambda s: len(universe.intersection(s)))
        chosen_sets.append(best_set)
        universe -= best_set

    return chosen_sets


universe = {int(x) for x in input().split(", ")}
numbers_of_sets = int(input())
sets_input = [{int(x) for x in input().split(", ")} for _ in range(numbers_of_sets)]

result = set_cover(universe, sets_input)

for i in range(len(result)):
    result[i] = sorted(result[i])

print(f"Sets to take ({len(result)}):")
[print("{ " + ', '.join(str(x) for x in s) + " }") for s in result]

"""With print as a function"""

# def result_print(chosen_sets):
#     result = f"Sets to take ({len(chosen_sets)}):\n"
#
#     for i in range(len(chosen_sets)):
#         chosen_sets[i] = sorted(chosen_sets[i])
#
#     for s in chosen_sets:
#         result += "{ " + ', '.join(str(x) for x in s) + " }\n"
#
#     return result
#
#
# def set_cover(universe, sets_input):
#     chosen_sets = []
#
#     while universe:
#         best_set = max(sets_input, key=lambda s: len(universe.intersection(s)))
#         chosen_sets.append(best_set)
#         universe -= best_set
#
#     return result_print(chosen_sets)
#
#
# universe = {int(x) for x in input().split(", ")}
# numbers_of_sets = int(input())
# sets_input = [{int(x) for x in input().split(", ")} for _ in range(numbers_of_sets)]
#
# print(set_cover(universe, sets_input))