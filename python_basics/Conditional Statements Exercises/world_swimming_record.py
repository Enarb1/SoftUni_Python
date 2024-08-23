from math import floor

record_to_beat = float(input())
distance = float(input())
one_m_swim = float(input())

delay = floor(distance / 15) * 12.5

total_time = (one_m_swim * distance) + delay
difference = abs(total_time - record_to_beat)
if total_time < record_to_beat :
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {difference:.2f} seconds slower.')