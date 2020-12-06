```python
def permute(nums):
    def backtrack(index):
        
        if index == len(nums) :
            res.append(comb)
            print(res)
            return res

        
        for y in nums:
            comb.append(y)

            backtrack( index + 1)

            comb.pop()
        
    res = []
    comb = []
    return backtrack(0)
```
