class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        characters = {chr(x) for x in range(97,123,1)}
        for k in characters:
            first,last = s.find(k),s.rfind(k)
            if first!=-1:
                res+=len(set(s[first+1:last]))
        return res
