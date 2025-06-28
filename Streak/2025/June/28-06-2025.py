class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(sorted(nums, reverse=True)[:k])
        res = []
        for num in nums:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1
        return res
