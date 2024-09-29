def sum_of_coins(coins, target):
    coins.sort(reverse=True)
    idx = 0
    used_coins = {}

    while target > 0 and idx < len(coins):
        current_coin = target // coins[idx]
        target = target % coins[idx]

        if current_coin > 0:
            used_coins[coins[idx]] = current_coin

        idx += 1

    if target != 0:
        return "Error"
    else:
        result = f"Number of coins to take: {sum(used_coins.values())}\n"

        for coin, count in used_coins.items():
            result += f"{count} coin(s) with value {coin}\n"

        return result


coins_all = [int(x) for x in input().split(", ")]
target_sum = int(input())
print(sum_of_coins(coins_all, target_sum))