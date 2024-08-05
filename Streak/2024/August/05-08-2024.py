class Solution(object):
    def kthDistinct(self, arr, k):
        d = defaultdict(lambda: 0)
        for x in arr:
            d[x] += 1
        
        ans = ""
        count = 0
        for x in arr:
            if d[x] == 1:
                ans = x
                count += 1
            
            if count == k:
                return ans
        return ""
