def tribonacci(numb):

    trib = [1,1,2]

    if numb == 1:
        return [1]
    elif numb == 2:
        return [1, 1]
    elif numb == 3:
        return trib

    for i in range(3,numb):
        next_value = trib[-1] + trib[-2] + trib[-3]
        trib.append(next_value)

    return trib

def print_tib(numb):
    sequence = tribonacci(numb)
    print(" ".join(map(str,sequence)))


count = int(input())
print_tib(count)
