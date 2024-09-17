from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [key for key,value in Counter(s1.split() + s2.split()).items() if value == 1]

        
