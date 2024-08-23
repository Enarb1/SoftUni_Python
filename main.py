
dictionary = {
            'odd': [1, 2, 3, 4, 10, 5],
            'even': [3, 4, 5, 7, 10, 2, 5, 5, 2]
              }

even_sort = sorted(dictionary['even'], key=lambda kvp: (-len(kvp[1]), kvp[1]))
print(even_sort)