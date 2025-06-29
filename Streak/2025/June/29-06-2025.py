class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        res = 0
        i, j = 0, len(nums)-1
        while i <= j:
            if target < nums[i] + nums[j]:
                j -= 1
            else:
                res += (1 << (j - i)) % MOD
                res %= MOD
                i += 1

        return res
        
