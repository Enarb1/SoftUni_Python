def lift_line(waiting_people, current_state_of_lift ):
    for index in range(len(current_state_of_lift)):
        if waiting_people > 3:
            current_num_of_people = abs(4 - current_state_of_lift[index])
            waiting_people -= current_num_of_people
            current_state_of_lift[index] += current_num_of_people
        else:
            current_state_of_lift[index] += waiting_people
            waiting_people = 0

    if waiting_people > 0:
        print(f"There isn't enough space! {waiting_people} people in a queue!")
    elif sum(current_state_of_lift) != len(current_state_of_lift) * 4:
        print("The lift has empty spots!")
    print(" ".join(str(num) for num in current_state_of_lift))


waiting =int(input())
lift = list(map(int,input().split()))
lift_line(waiting,lift)



