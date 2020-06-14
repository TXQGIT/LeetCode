def coinChange(coins, amount):
    # #解法1：dp[i]表示金额i的最小硬币数
    # dp = [float('inf')]*(amount+1)
    # dp[0] = 0
    # for i in range(1, amount + 1):
    #     for coin in coins:
    #         if i >= coin:
    #             dp[i] = min(dp[i], dp[i - coin] + 1)
    # return dp[amount] if dp[amount] != float('inf') else -1

    # 解法2：完全背包问题
    # dp[i][j]前i个面额的硬币凑金额为j的最小硬币数
    n = len(coins)
    dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(0, amount + 1):
            if j >= coins[i - 1]:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][amount]

coins = [1,2,5]
amount = 11
# coins = [2147483647]
# amount = 2
# coins = [2]
# amount = 3
print(coinChange(coins, amount))