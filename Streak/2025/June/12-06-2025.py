class Solution:
    def maxAdjacentDistance(self, a: List[int]) -> int:
        return max(abs(v-a[i-1])for i,v in enumerate(a))
