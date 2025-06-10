class Solution:
    def maxDifference(self, s: str) -> int:
        from collections import Counter

        freq = Counter(s)
        max_odd = 0
        min_even = len(s)

        for count in freq.values():
            if count % 2 == 1:
                max_odd = max(max_odd, count)
            else:
                min_even = min(min_even, count)

        return max_odd - min_even
