class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        a,c=0,0
        co=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':c+=1
            else:
                a+=2**co
                if a<=k:c+=1
            co+=1
        return c
