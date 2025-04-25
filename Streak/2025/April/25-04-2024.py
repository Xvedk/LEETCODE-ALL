class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        c=s=0 ; m = {0:1}
        for n in nums:
            if n % modulo == k: s = (s+1) % modulo
            c += m.get((s-k) % modulo, 0)
            m[s] = m.get(s, 0) + 1
        return c
