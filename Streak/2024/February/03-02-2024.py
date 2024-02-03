class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        @cache
        def f(i): # recursion
            if i<=0: return 0
            ans=0
            maxA=0
            for j in range(1, min(k+1, i+1)):
                maxA=max(maxA, arr[i-j])
                ans=max(ans, f(i-j)+j*maxA)
            return ans
        return f(n)
        
