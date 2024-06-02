class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        n0=n//2
        for i in range(n0):
            tmp=s[i]
            s[i]=s[n-1-i]
            s[n-1-i]=tmp
