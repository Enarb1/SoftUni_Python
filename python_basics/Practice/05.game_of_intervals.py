steps = int(input())

total_result = 0
from0to9 = 0
from10to19 = 0
from20to29 = 0
from30to39 = 0
from40to50 = 0
invalid_numbers = 0

for _ in range(1,steps + 1):
    num = int(input())
    result = 0
    if 0 <= num < 10:
        from0to9 += 1
        result = 0.2 * num
    if 10 <= num < 20:
        from10to19 += 1
        result = 0.3 * num
    if 20 <= num < 30:
        from20to29 += 1
        result = 0.4 * num
    if 30 <= num < 40:
        from30to39 += 1
        result = 50
    if 40 <= num <= 50:
        from40to50 += 1
        result = 100
    total_result += result
    if num < 0 or num > 50:
        invalid_numbers += 1
        total_result = total_result / 2

print(f"{total_result:.2f}")
print(f"From 0 to 9: {from0to9 / steps * 100:.2f}%")
print(f"From 10 to 19: {from10to19 / steps * 100:.2f}%")
print(f"From 20 to 29: {from20to29 / steps * 100:.2f}%")
print(f"From 30 to 39: {from30to39 / steps * 100:.2f}%")
print(f"From 40 to 50: {from40to50 / steps * 100:.2f}%")
print(f"Invalid numbers: {invalid_numbers / steps * 100:.2f}%")



