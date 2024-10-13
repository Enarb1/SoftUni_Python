from collections import deque
daily_portions = [int(p) for p in input().split(", ")]
daily_stamina = deque([int(s) for s in input().split(", ")])

peaks = deque([("Vihren", 80),("Kutelo", 90), ("Banski Suhodol", 100),("Polezhan", 60),("Kamenitza", 70)])

conquered_peaks = []

while daily_portions and daily_stamina and peaks:
    peak, energy_needed = peaks.popleft()
    energy = daily_portions.pop() + daily_stamina.popleft()

    if energy >= energy_needed:
        conquered_peaks.append(peak)
    else:
        peaks.appendleft((peak,energy_needed))

if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    print('\n'.join(conquered_peaks))