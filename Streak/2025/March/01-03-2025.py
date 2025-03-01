class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        zeros = 0
        res = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
    
        for n in nums:
            if n == 0:
                zeros += 1
            else:
                res.append(n)
                
        return res + ([0] * (zeros))
