class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        
        # dp[n, m, k] = dp[n - 1, m, k] * (m - 1) + dp[n - 1, m, k - 1]
        # dp[n, k] = dp[n - 1, k] * (m - 1) + dp[n - 1, k - 1]
        
        MOD = 1000000007
        if n == 1:
            return m
        
        if m == 1:
            if k == n - 1:
                return 1
            else:
                return 0

        if k == 0:
            return int(m * (m - 1) ** (n - 1) % (MOD))

        prev_row = [0] * (k + 1)

        for i in range(1, n + 1): # n
            # base case when k == 0: m * ((m - 1) ** (i - 1))
            current_row = [m * ((m - 1) ** (i - 1)) % (MOD)] + [0] * k
            
            for j in range(1, k + 1): # k
                current_row[j] = (prev_row[j] * (m - 1) + prev_row[j - 1]) % (MOD)
            
            prev_row = current_row
        
        return prev_row[-1] % (MOD)
