class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # dp[i][j]: number of ways to get sum j with i dice
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # Base case: one die
        for j in range(1, min(k, target) + 1):
            dp[1][j] = 1

        # Fill the dp table
        for i in range(2, n + 1):
            for j in range(1, target + 1):
                for face in range(1, k + 1):
                    if j - face >= 0:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - face]) % MOD

        return dp[n][target]
