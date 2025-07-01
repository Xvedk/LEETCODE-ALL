class Solution:
    def possibleStringCount(self,s: str) -> int:
        s=s[::-1]
        c=0
        k=s[0]
        for i in range(len(s)) :
            if s[i]==k:
                c+=1  # here only first frequency is taken fully
            if s[i]!=k:
                k=s[i] # in all frequencies one count is missing here so, adding frequencies - 1
        return c
