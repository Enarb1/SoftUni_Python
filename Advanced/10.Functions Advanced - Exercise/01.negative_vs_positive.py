def negative_vs_positive(nums):

    negative_total = sum(num for num in nums if num < 0)
    positive_total = sum(num for num in nums if num > 0)

    print(negative_total)
    print(positive_total)

    if positive_total > abs(negative_total):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]
negative_vs_positive(numbers)