class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        a = 0 
        b = sum(nums) 
        n = len(nums) 
        cou = 0 
        for i in range(n - 1): 
            a += nums[i] 
            b -= nums[i] 
            if a >= b: 
                cou += 1 
        return cou
