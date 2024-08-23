
def perfect_num(number):
    num = number
    divisor = []
    valid = False
    for div in range(1, num):
        if num % div == 0:
            divisor.append(div)

    if num == sum(divisor):
        valid = True

    return valid


number_int = int(input())
if perfect_num(number_int) == True:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")



