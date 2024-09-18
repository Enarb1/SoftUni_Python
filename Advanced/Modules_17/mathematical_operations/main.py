from Advanced.Modules_17.mathematical_operations.core import mapper

expression = input().split()
first_num, sign, second_num = expression

num1 = float(first_num)
num2 = int(second_num)

result = mapper[sign](num1, num2)

print(f"{result:.2f}")