class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ltrs = {"a": 0, "b": 0, "c": 0}
        subs = 0
        left = 0
        
        for right in range(n):
            ltrs[s[right]] += 1
            while ltrs['a'] > 0 and ltrs['b'] > 0 and ltrs['c'] > 0:
                subs += n - right
                ltrs[s[left]] -= 1
                left += 1
                
        return subs        
