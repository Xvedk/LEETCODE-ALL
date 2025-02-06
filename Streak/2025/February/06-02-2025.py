class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)
        n = len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n):
                freq_map[nums[i]*nums[j]] += 1

        res = 0
        for v in freq_map.values():
            if v > 1:
                res += v*(v - 1)*4
        
        return res
        
