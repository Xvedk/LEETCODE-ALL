class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        ans = 0
        count = 1  # Count of the current homogenous substring

        for i in range(1, n):
            if s[i] == s[i - 1]:
                count += 1
            else:
                ans = (ans + (count * (count + 1) // 2)) % MOD
                count = 1

        # Handle the remaining homogenous substring at the end
        ans = (ans + (count * (count + 1) // 2)) % MOD

        return ans
