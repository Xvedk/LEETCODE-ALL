class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunk = 0
        max_val = [0] * len(arr)
        max_val[0] = arr[0]

        for i in range(1, len(arr)):
            max_val[i] = max(max_val[i - 1], arr[i])

        for i in range(len(arr)):
            if max_val[i] == i:
                chunk += 1
        
        return chunk
