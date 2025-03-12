class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # bisect_left() gives index to left of 0, indices start to bisect are negative
        neg = bisect_left(nums, 0) 

        # bisect_right() gives index to right of 0, indices bisect to end are positive
        pos = len(nums) - bisect_right(nums, 0) 

        return max(neg, pos)
