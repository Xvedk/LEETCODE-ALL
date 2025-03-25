class Solution:
    def checkValidCuts(self, n: int, r: List[List[int]]) -> bool:
        x_intervals = [[r[i][0], r[i][2]] for i in range(len(r))]
        y_intervals = [[r[i][1], r[i][3]] for i in range(len(r))]

        x_intervals.sort()
        y_intervals.sort()
        
        def helper(intervals):
            res = 0
            head, max_end = intervals[0][0], intervals[0][1]
            for line in intervals[1:]:
                start, end = line
                if start >= max_end:
                    res += 1
                    head = start
                    max_end = end
                else:
                    max_end = max_end if max_end > end else end
            return res >= 2
        
        return helper(x_intervals) or helper(y_intervals)
