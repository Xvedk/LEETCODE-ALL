class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = min(nums), max(nums)
        n = len(nums)
        
        while left < right:
            middle = (left + right) // 2
            thefts = 0
            index = 0

            while index < n:
                if nums[index] <= middle:
                    thefts += 1
                    index += 2  # Skip adjacent house to avoid consecutive thefts
                else:
                    index += 1

            if thefts >= k:
                right = middle  # Try for a smaller maximum capability
            else:
                left = middle + 1  # Increase capability to allow more thefts
                
        return left
