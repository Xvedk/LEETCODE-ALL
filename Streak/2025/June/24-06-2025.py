class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        idx = []
        for i in range(len(nums)):
            if nums[i] == key:
                idx.append(i)
        s = set()
        l = len(nums)

        for ind in idx:
            a = max(0,ind-k)
            b = min(ind+k,l)
            for num in range(a, b+1):
                if num < l:
                    s.add(num)
        return list(s)
            
            
