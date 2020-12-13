# 跳跃游戏
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        n = len(nums)
        for i,x in enumerate(nums):
            if i <= reach:
                reach = max(reach, i+nums[i])
                if reach >= n-1:
                    return True
            else:
                return False
        return False