## 给定一个非空的正整数数组 nums ，请判断能否将这些数字分成元素和相等的两部分。
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2 != 0 or len(nums) <= 1:
            return False
        dp = {0}
        for num in nums:
            tmp = [e+num for e in dp]
            if s/2 in tmp:
                return True
            dp.update(tmp)
        return False
## 思路就是，我从nums【0】开始，一直遍历会出现什么可能性
## 即每次加上一个（set+nums【i】）到set里面
## 注意一下起始判据：如果sum不可以被2整除，或者len《=1 ，gg
## 注意一下使用了dict，来实现set的操作
