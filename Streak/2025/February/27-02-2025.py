class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 4:
            return 0
        keys = set(arr)
        longest = 0
        for i in range(n):
            for j in range(i+1, n):
                seq = 2
                a, b = arr[i], arr[j]
                while a + b in keys:
                    a, b = b, a + b
                    seq += 1
                    
                if seq > 2:
                    longest = max(longest, seq)
                
        return longest        
