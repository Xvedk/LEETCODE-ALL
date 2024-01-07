class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for i in range(n)]
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                d = nums[i] - nums[j]
                dp[i][d] = dp[i].get(d, 0) + dp[j].get(d, 0) + 1
        ans = 0
        for d in dp:
            ans += sum(d.values())
        return ans - (n*(n-1))//2
