class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        free = 0
        left = 0
        poss = 0

        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == '(':
                    left += 1 
                    poss = max(1, poss+1)
                else:
                    if left > 0:
                        left -= 1
                    elif free > 0:
                        free -= 1
                    else:
                        return False
                    poss -= 1
            else:
                free += 1
                poss -= 1
        if poss > 0:
            return False
        return True
                
