class Solution:
    def putMarbles(self, l: List[int], k: int) -> int:
        n = len(l)
        if k == 1 or k == n:
            return 0
        
        hp = []
        for i in range(n - 1):
            hp.append(l[i] + l[i + 1])
        
        hp.sort()
        return sum(hp[-(k-1):]) - sum(hp[:k-1])
