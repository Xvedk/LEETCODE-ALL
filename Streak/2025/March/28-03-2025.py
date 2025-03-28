class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        border, ans = [(grid[0][0], 0, 0)], [0] * len(queries)
        cnt, grid[0][0] = 0, 0
        for k in sorted(range(len(queries)), key = lambda i: queries[i]):
            while border and border[0][0] < queries[k]:
                _, i, j = heappop(border)
                cnt += 1
                for ii, jj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj]:
                        heappush(border, (grid[ii][jj], ii, jj))
                        grid[ii][jj] = 0
            ans[k] = cnt
        return ans            
