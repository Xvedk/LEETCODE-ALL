class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        m = Counter(word)
        va = list(m.values())
        i = 0
        j = len(va) - 1
        ans = float('inf')
        print(va)
        for x in va:
            count = 0
            for y in va:
                if y < x:
                    count += y
                elif y > x + k:
                    count += y - x - k
            ans = min(ans, count)
        return ans
        

                
