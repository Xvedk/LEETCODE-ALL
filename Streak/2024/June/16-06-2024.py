class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1  # The smallest number we cannot form yet
        i = 0     # Index to iterate through nums
        patches = 0  # Number of patches added
        
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                # If the current number can help to form miss
                miss += nums[i]
                i += 1
            else:
                # Add miss as a patch
                miss += miss
                patches += 1
        
        return patches
