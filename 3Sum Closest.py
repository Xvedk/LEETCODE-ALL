class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                
                if threeSum == target:
                    return threeSum
                
                if abs(threeSum - target) < abs(closest_sum - target):
                    closest_sum = threeSum
                
                if threeSum < target:
                    l += 1
                else:
                    r -= 1
        
        return closest_sum
