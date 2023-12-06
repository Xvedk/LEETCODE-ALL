class Solution:
    def solve(self, week):
        result = 0
        for i in range(week):
            result += 28 + (i * 7)
        return result

    def totalMoney(self, n):
        week = n // 7
        ans = self.solve(week)
        day = n % 7
        if day == 0:
            return ans
        else:
            current_week = week + 1
            while day > 0:
                ans += current_week
                current_week += 1
                day -= 1
        return ans
