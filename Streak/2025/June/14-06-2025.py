class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        s = str(num)

        for c in s: 
            if c != '9': 
                s_max = s.replace(c, '9')
                break

        else: 
            s_max = s

        for c in s: 
            if c != '0':
                s_min = s.replace(c, '0')
                break
        
        else:
            s_min = s

        return int(s_max) - int(s_min)
