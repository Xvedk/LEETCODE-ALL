class Solution:
    def minPairSum(self, nums):
        n, max_val = len(nums), 0

        nums.sort()

        i,j = 0,n-1

        while i<j:
            max_val = max(max_val,nums[i]+nums[j])
            i += 1
            j -= 1

        return max_val

        
