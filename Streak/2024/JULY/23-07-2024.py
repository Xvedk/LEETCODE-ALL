class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums) #O(n)
        freq = [[] for _ in range(len(nums)+1)] #O(n)

        for key,val in count.items(): #O(n)
            freq[val].append(key)

        res = []
        for i,l in enumerate(freq): #O(nlogn)
            for item in sorted(l,reverse=True):
                res+=[item]*i
        
        return res
