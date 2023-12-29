class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        size = len(jobDifficulty)
        max_jobDifficulty = max(jobDifficulty)

        dp = [[[ -1 for _ in range(max_jobDifficulty + 1)] for _ in range(d + 1)] for _ in range(size + 1)]

        def rec(idx, max_day, days_done):
            if idx == size:
                if days_done == d:
                    return 0
                else:
                    return float('inf')

            if dp[idx][days_done][max_day] != -1:
                return dp[idx][days_done][max_day]

            new_day = float('inf')

            max_day = max(max_day, jobDifficulty[idx])

            if days_done < d - 1 or (days_done < d and idx == size - 1):
                new_day = max_day + rec(idx + 1, 0, days_done + 1)

            same_day = rec(idx + 1, max_day, days_done)

            dp[idx][days_done][max_day] = min(new_day, same_day)
            return dp[idx][days_done][max_day]

        ans = rec(0, 0, 0)
        return ans if ans < float('inf') else -1
