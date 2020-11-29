class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,x in enumerate(nums):
            s_list = nums[i+1:]
            if target-x in s_list:
                return [nums.index(x), s_list.index(target-x)+i+1]