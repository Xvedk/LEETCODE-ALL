class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx_or = 0
        n = len(nums)
        
        for x in nums:
            mx_or |= x
        
        total_subsets = (1 << n) - 1
        
        cnt = 1
        for i in range(1, total_subsets + 1):
            or_sub = 0
            for j in range(n):
                if i & (1 << j):
                    or_sub |= nums[j]
            if or_sub == mx_or:
                cnt += 1
        
        return cnt
