class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows = dict.fromkeys(range(m), n)
        cols = dict.fromkeys(range(n), m)
        position = {mat[r][c]: [r, c] for r in range(m) for c in range(n)}
        for i, n in enumerate(arr):
            r, c = position[n]
            rows[r] -= 1
            cols[c] -= 1
            if not rows[r] or not cols[c]:
                return i
