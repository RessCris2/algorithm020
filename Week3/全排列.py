# 思路： 第n层的全排列等于第n-1层的全排列和第n层的混排结果。
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(index):
        
	        if index == len(nums) :
	            res.append(comb[:])
	            # print('res',res)
	            # print(len(res))
	            return res

	        
	        for y in nums:
	            if y not in comb:
	                comb.append(y)
	                #print('comb',comb)

	                backtrack( index + 1)

	                comb.pop()
	        
	    res = []
	    comb = []
	    backtrack(0)
	    return res

# 理解错题了，这个代码返回的是所有可能的组合。加上一句判断也搞定了。
