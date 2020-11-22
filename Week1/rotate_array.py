# 这个解法超出时间限制，是因为我进行了两次大型复制吗？而且题目要求尽量O(1)空间。
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            x = nums[-1]
            q = nums[:-1]
            nums[1:] = q
            nums[0] = x


# 使用两次reverse的方式。 
def Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums.reverse()
        # 这种方式无返回
        #nums[:] = nums[:k].reverse() + nums[k:].reverse()    
        #nums[:] = list(reversed(nums[:k])) +list(reversed(nums[k:]))
        nums[:] = nums[:k][::-1] + nums[k:][::-1]



# 使用环状替换的算法最为巧妙，不过终止条件的部分还是想的不是非常明白。

# 还是迭代放置到正确的位置上