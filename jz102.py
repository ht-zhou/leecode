# 给定一个正整数数组 nums 和一个整数 target 。

# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ## 暴力解法非常憨批
        # sum_list = [0]
        # for num in nums:
        #     tmp1 = [e + num for e in sum_list]
        #     tmp2 = [e - num for e in sum_list]
        #     tmp1.extend(tmp2)
        #     sum_list = tmp1
        # return sum_list.count(target)

        ## 可以转化成101的问题求解，寻找x个进pos，剩下进neg
        ## 二维dp
        # total = sum(nums)
        # if abs(target) > total or (total+target)%2!=0:
        #     return 0
        # pos = (total + target) / 2
        # neg = (total - target) / 2
        # cap = min(pos, neg)
        # n = len(nums)
        
        # # 初始化
        # dp = [[0] * (cap+1) for _ in range(n+1)]
        # # dp[i][j]: 从前i个元素中选出若干个其和为j的方案数
        # dp[0][0] = 1        # 其他 dp[0][j]均为0
        # # dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
        # for i in range(1, n+1):
        #     for j in range(cap+1):
        #         # nums[i-1]是【i】对应的，因为i是从1开始的
        #         if j < nums[i-1]:
        #             dp[i][j] = dp[i-1][j]
        #         else:
        #             dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
        # return dp[n][cap]

        # 可以继续转化成一维的dp
        # 每次更新都只涉及同一行，可以行之间滚动
        # total = sum(nums)
        # if abs(target) > total or (total+target)%2!=0:
        #     return 0
        # pos = (total + target) / 2
        # neg = (total - target) / 2
        # cap = min(pos, neg)
        # n = len(nums)

        # dp = [0] * (cap+1)
        # dp[0] = 1

        # for i in range(1, n+1):
        #     dp2 = [0] * (cap+1)
        #     for j in range(cap+1):
        #         if j > nums[i-1]:
        #             dp2[j]=dp[j]
        #         else:
        #             dp2[j] = dp[j] + dp[j-nums[i-1]]
        #     dp = dp2
        
        # return dp[cap] 

        # 可以省略dp2
        total = sum(nums)
        if abs(target) > total or (total+target)%2!=0:
            return 0
        pos = (total + target) / 2
        neg = (total - target) / 2
        cap = min(pos, neg)
        n = len(nums)

        dp = [0] * (cap+1)
        dp[0] = 1

        for num in nums:
            for j in range(cap, num-1, -1):
                dp[j] = dp[j] + dp[j-num]
        return dp[cap]
