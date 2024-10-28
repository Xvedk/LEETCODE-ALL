
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        dp={i:1 for i in nums}
        longest=1
        for i in nums:
            sq= i**2
            if sq in dp:
                dp[sq]= dp[i]+1
                if dp[sq]==5: return dp[sq]
                if dp[sq]>longest:
                    longest=dp[sq]
        return longest if longest!=1 else -1
        
