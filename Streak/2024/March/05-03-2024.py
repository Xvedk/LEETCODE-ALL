class Solution:
    def minimumLength(self, s: str) -> int:
        l,r=0,len(s)-1

        while l<r and s[l]==s[r]:
            check=s[l]
            l+=1
            r-=1
            while l<=r and s[l]==check:
                l+=1
            while l<=r and s[r]==check:
                r-=1

        return r-l+1
        
