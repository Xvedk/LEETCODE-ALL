class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        return max(max(accumulate(nums)), 0) - min(min(accumulate(nums)), 0)
