class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(int(log10(n))&1 for n in nums)
