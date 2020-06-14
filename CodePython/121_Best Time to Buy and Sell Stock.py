#!/usr/bin/env python

# 问题分析：
# dp[i][k][0]:在第i天，至多进行了k次交易(以买入计算)，手里没有持有股票时的最大收益
# dp[i][k][1]:在第i天，至多进行了k次交易(以买入计算)，手里持有股票时的最大收益

# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
# 解释：今天我没有持有股票，有两种可能：
# 要么是我昨天就没有持有，然后今天选择 rest，所以我今天还是没有持有；
# 要么是我昨天持有股票，但是今天我 sell 了，所以我今天没有持有股票了。

# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
# 解释：今天我持有着股票，有两种可能：
# 要么我昨天就持有着股票，然后今天选择 rest，所以我今天还持有着股票；
# 要么我昨天本没有持有，但今天我选择 buy，所以今天我就持有股票了。

# dp[-1][k][0] = 0
# 解释：因为 i 是从 0 开始的，所以 i = -1 意味着还没有开始，这时候的利润当然是 0 。
# dp[-1][k][1] = -infinity
# 解释：还没开始的时候，是不可能持有股票的，用负无穷表示这种不可能。
# dp[i][0][0] = 0
# 解释：因为 k 是从 1 开始的，所以 k = 0 意味着根本不允许交易，这时候利润当然是 0 。
# dp[i][0][1] = -infinity
# 解释：不允许交易的情况下，是不可能持有股票的，用负无穷表示这种不可能。

import numpy as np
# prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
# 问题1：限制k=1
dp = np.zeros([len(prices)+1, 2, 2], dtype=float)
dp[0][1][0] = dp[:][0][0] = 0
dp[0][1][1] = dp[:][0][1] = float('-inf')
for k in range(1, 2):
    for i in range(1, len(prices)+1):
        try:
            dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i-1])
            dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i-1])
        except:
            print('value of k and i is:', k,i)
print(dp)
print(dp[len(prices)][1][0])