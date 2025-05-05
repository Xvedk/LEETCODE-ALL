class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        arr = [0] * max(3, n)
        arr[0] = 1  # n = 1
        arr[1] = 2  # n = 2
        arr[2] = 5  # n = 3
        for i in range(3, n):
            arr[i] = (2 * arr[i - 1] + arr[i - 3]) % MOD
        return arr[n - 1]
