#n = int(input())

guest_list = {input() for guest in range(int(input()))}
#guest_list = set()

# for _ in range(n):
#     guest = input()
#     guest_list.add(guest)

data = input()

while data != "END":
    if data in guest_list:
        guest_list.remove(data)
    data = input()

print(len(guest_list))
sorted_guest_list = sorted(guest_list)
print(*sorted_guest_list, sep='\n')
