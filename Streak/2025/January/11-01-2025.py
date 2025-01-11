class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        from collections import Counter
        freq = Counter(s)
        
        odds = sum(1 for count in freq.values() if count % 2 != 0)
        
        return odds <= k
