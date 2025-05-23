class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        deltas = []
        total = 0
        
        for num in nums:
            xor_val = num ^ k
            total += num
            deltas.append(xor_val - num)

        deltas.sort(reverse=True)
        i = 0
        while i + 1 < len(deltas) and deltas[i] + deltas[i+1] > 0:
            total += deltas[i] + deltas[i+1]
            i += 2

        return total
