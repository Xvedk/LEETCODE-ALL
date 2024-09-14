class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_and = nums[0]
        # Find the maximum bitwise AND (which is the max element in this case)
        for num in nums:
            max_and = max(max_and, num)
        
        ans = 0
        temp = 0
        
        for num in nums:
            if num == max_and:
                temp += 1
                ans = max(ans, temp)
            else:
                temp = 0
        
        return ans
