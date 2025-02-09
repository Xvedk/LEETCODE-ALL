class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = comb(n, 2)
        mp = Counter(nums[i] - i for i in range(n))
        good = sum(comb(i, 2) for i in mp.values() if i > 1)  
        return total - good
