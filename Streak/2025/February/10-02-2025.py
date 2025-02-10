class Solution:
    def clearDigits(self, s: str) -> str:
        j=0
        s=list(s)
        for i, c in enumerate(s):
            if c.isdigit() and j>0: 
                j-=1
            else:
                s[j]=c
                j+=1
        s=s[:j] 
        return "".join(s)
        
        
