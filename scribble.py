n = 50

mapper = {
    (0, 60): "Darth Vader Ducky",
    (61, 120): "Thor Ducky",
    (121, 180): "Big Blue Rubber Ducky",
    (181, 240): "Small Yellow Rubber Ducky"
}


for (start, end), key in mapper.items():
    if start <= n <= end:
        print(key)



