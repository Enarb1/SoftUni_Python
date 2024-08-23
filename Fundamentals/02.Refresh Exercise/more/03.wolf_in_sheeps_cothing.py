input_string = input()

animals_list = input_string.split(", ")
sheep = 0
for animal in reversed(animals_list):
    if animal == "wolf" and sheep == 0:
        print("Please go away and stop eating my sheep")
    elif animal == "wolf":
        print(f"Oi! Sheep number {sheep}! You are about to be eaten by a wolf!")
    if animal == "sheep":
        sheep += 1


