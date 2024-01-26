class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        modulo = 1_000_000_007
        
        @cache
        def dp(x, y, moves):
            if not (0 <= x < m) or not (0 <= y < n):
                return 1
            if moves == 0:
                return 0
            
            result = 0
            for xx, yy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                result += dp(xx, yy, moves - 1)
            return result % modulo

        return dp(startRow, startColumn, maxMove)
