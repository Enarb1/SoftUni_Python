def rev_array(idx, elements):
    if idx == len(elements) // 2:
        return elements[idx]
    swap_idx = len(elements) - 1 - idx
    elements[idx], elements[swap_idx] = elements[swap_idx], elements[idx]
    rev_array(idx + 1, elements)


elements = input().split()
rev_array(0, elements)

print(*elements)


