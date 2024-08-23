ANNUAL_TAX = int(input())

sneakers = ANNUAL_TAX - (ANNUAL_TAX * 0.40)
jersey = sneakers - (sneakers * 0.20)
ball = jersey * 0.25
accessoaries = ball * 0.20

total = ANNUAL_TAX + sneakers + jersey + ball +accessoaries

print(total)