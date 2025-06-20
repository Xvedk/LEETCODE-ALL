class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        dirs = defaultdict(int)
        res = 0

        for c in s:
            dirs[c] += 1
            minX, maxX = min(dirs['E'], dirs['W']), max(dirs['E'], dirs['W'])
            minY, maxY = min(dirs['N'], dirs['S']), max(dirs['N'], dirs['S'])
            res = max(res, maxX + maxY - minX - minY + 2 * min(minX + minY, k))
        
        return res
