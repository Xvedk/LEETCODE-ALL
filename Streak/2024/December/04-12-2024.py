class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n1, n2=len(str1), len(str2)
        str2+='@'
        c2=str2[0]
        i, j=0, 0
        while i<n1 and j<n2:
            c1=str1[i]
            if c1==c2 or ord(c1)+1==ord(c2) or (c1=='z' and c2=='a'):
                j+=1
                c2=str2[j]
            i+=1
        return j==n2
