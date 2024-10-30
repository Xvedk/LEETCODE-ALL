from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        increasing = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    increasing[i] = max(increasing[i], increasing[j] + 1)
        
        decreasing = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    decreasing[i] = max(decreasing[i], decreasing[j] + 1)
        
        max_mountain_length = 0
        for i in range(1, n - 1):
            if increasing[i] > 1 and decreasing[i] > 1:
                max_mountain_length = max(max_mountain_length, increasing[i] + decreasing[i] - 1)
        
        return n - max_mountain_length
