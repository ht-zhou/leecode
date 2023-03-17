# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

# 你可以认为每种硬币的数量是无限的。

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 分析一下和101和102的区别
        # 101 -> 有没有
        # 102 -> 有多少
        # 102 -> 最小的, 每一种可以有多个

        # # 很暴力
        # if amount == 0:
        #     return 0
        # if min(coins) > amount:
        #     return -1
        
        # n = len(coins)
        # max_num = (amount // min(coins))
        # set = {0}
        # for k in range(max_num):
        #     tmp = []
        #     for coin in coins: 
        #         tmp.extend([coin + e for e in set])
        #         if amount in tmp:
        #             return k + 1
        #     set.update(tmp)
        # return -1

        #DP怎么做呢
        # 对于本题，定义二维数组dp[i][j] 表示：从前i 种硬币中组成金额 j 所需最少的硬币数量。
        # 为便于状态更新，减少对边界的判断，初始二维 dp 数组维度为 (N+1) *,意味着第 i 种硬币为coins[i-1], 第0种硬币为空。

        # # 2层循环
        # if amount == 0:
        #     return 0
        # if min(coins) > amount:
        #     return -1
        # n = len(coins)
        # dp = [[1024] * (amount+1) for _ in range(n+1)]    # 初始化为一个较大的值，如 +inf 或 amount+1
        # # 合法的初始化
        # dp[0][0] = 0    # 其他 dp[0][j]均不合法
        # for i in range(1, n+1):
        #     for j in range(amount + 1):
        #         if j < coins[i-1]:
        #             dp[i][j] = dp[i-1][j]
        #         else:
        #             dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]]+1)
        # ans = dp[n][amount]
        # if ans == 1024:
        #     return -1
        # return ans

        # 2层循环，一维dp
        # 每一行的 dp 状态值都只与其正上方和左方的状态值有关，因此可对状态空间优化
        if amount == 0:
            return 0
        if min(coins) > amount:
            return -1
        n = len(coins)
        dp = [1024] * (amount+1)   # 初始化为一个较大的值，如 +inf 或 amount+1
        # 合法的初始化
        dp[0]= 0    # 其他 dp[0][j]均不合法
        for coin in coins:                          # 遍历硬币
            for j in range(coin, amount + 1):        # 遍历背包
                    dp[j] = min(dp[j], dp[j-coin]+1)
        ans = dp[amount]
        if ans == 1024:
            return -1
        return ans

        # !!!「完全背包问题」内层循环正序，而「0-1 背包问题」中内层循环反序
