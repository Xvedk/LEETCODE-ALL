import collections

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @cache
        def dp(i): # return int, min delete
            if i == len(s):
                return 0
            
            res = float('inf')

            # take s[i]
            for word in dictionary:
                if len(word) + i > len(s): # word too long
                    continue
                
                sub_s = s[i: i + len(word)]
                
                # can take word
                if sub_s == word:
                    res = min(res, dp(i + len(word)))

            # skip s[i]
            res = min(res, dp(i + 1) + 1)

            return res

        return dp(0)
