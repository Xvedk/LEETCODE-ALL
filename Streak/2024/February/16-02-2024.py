class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        sorted_freq = sorted(freq.values())
        unique = len(sorted_freq)
        for i in sorted_freq:
            if k >= i:
                k-=i
                unique -= 1
            else:
                break
        return unique
