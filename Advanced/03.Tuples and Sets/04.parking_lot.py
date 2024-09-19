"""With Lambda functions mapper. More beautiful way"""
n = int(input())

parking = set()
mapper = {
    'IN': lambda x: parking.add(x),
    'OUT': lambda x: parking.remove(x) if x in parking else None
}
for _ in range(n):
    command, car_plate = input().split(', ')
    mapper[command](car_plate)

if parking:
    print(*parking, sep='\n')
else:
    print("Parking Lot is Empty")

""""From the lecture:"""

# n = int(input())
#
# parking = set()
#
# for _ in range(n):
#     command, car_plate = input().split(', ')
#     if command == 'IN':
#         parking.add(car_plate)
#     elif command == 'OUT':
#         if car_plate in parking:
#             parking.remove(car_plate)
#
# if parking:
#     print(*parking,sep='\n')
# else:
#     print(f'Parking Lot is Empty')
