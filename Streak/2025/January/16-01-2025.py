class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        n = len(nums1)
        m = len(nums2)
        if m % 2 != 0:
            for i in nums1:
                result ^= i
        if n % 2 != 0:
            for j in nums2:
                result ^= j
        return result
