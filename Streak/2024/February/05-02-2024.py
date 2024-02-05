class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        chars = sorted(set(s), key=s.index)
        for i in range(len(chars)):
            if s.count(chars[i]) == 1:
                return s.find(chars[i])
        
        return -1
