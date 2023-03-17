# 给定一个由 不同 正整数组成的数组 nums ，和一个目标整数 target 。请从 nums 中找出并返回总和为 target 的元素组合的个数。
# 数组中的数字可以在一次排列中出现任意次，但是顺序不同的序列被视作不同的组合。

# dp[j] = sum([dp[j-num] for num in nums])
# 除了初始化dp[0]=1
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        
        dp = [0] * (target + 1)
        dp[0] = 1
        for j in range(0, target + 1):
            if j ==0:
                tmp = 1
            else:
                tmp = 0
            for num in nums:
                if j >= num:
                    tmp += dp[j - num]
            dp[j] = tmp
        return (dp[target])
        
