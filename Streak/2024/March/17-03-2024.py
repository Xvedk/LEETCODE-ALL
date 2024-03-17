class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        target = newInterval[0]
        l, r = 0, len(intervals)-1
        while l<=r:
            mid = (l+(r-l)//2)
            if intervals[mid][0] < target:
                l = mid+1
            else:
                r = mid-1
        intervals.insert(l, newInterval)            
        res = []
        for i in intervals:
            if not res:
                res.append(i)
            else:
                if res[-1][1] >= i[0]:
                    res[-1][1] = max(res[-1][1], i[1])
                else:
                    res.append(i)
        return res
