class Solution:
    def longestMonotonicSubarray(self, n: List[int]) -> int:
        return max(max(accumulate(pairwise(n), lambda c,m:(1,c+1)[f(*m)], initial=1)) for f in(lt,gt))
