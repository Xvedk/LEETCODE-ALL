class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        ind = 0
        for e, s, p in sorted(zip(endTime, startTime, profit)):
            startTime[ind] = s
            endTime[ind]   = e
            profit[ind]    = p
            ind += 1
        
        dp = [profit[0]] + ([0] * ((n := len(profit))-1))

        for i in range(1, n):

            index = bisect_right(endTime, startTime[i]) - 1
            dp[i] = max(dp[i - 1], (dp[index] if index >= 0 else 0) + profit[i])

        return dp[-1]
