box_of_clothes = input().split()
rack_capacity = int(input())
racks = 1
rack_space = 0

while box_of_clothes:

        top_ = int(box_of_clothes.pop())
        if rack_space + top_ > rack_capacity:
            racks += 1
            rack_space = 0
        rack_space += top_

print(racks)




