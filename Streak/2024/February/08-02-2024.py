class Solution:
    def numSquares(self, n: int, memo={}) -> int:
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        min_sq = float('inf')
        for i in range(1, int(n**0.5) + 1):
            min_sq = min(min_sq, 1 + self.numSquares(n - i * i, memo))
        memo[n] = min_sq
        return min_sq
