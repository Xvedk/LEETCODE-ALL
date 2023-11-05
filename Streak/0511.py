class Solution(object):
    def getWinner(self, arr, k):
        d = dict()
        n = len(arr)
        mx = arr[0]
        for i in range(1, n):
            mx = max(mx, arr[i])
            d[mx] = d[mx] + 1 if mx in d.keys() else 1
            if d[mx] >= k:
                return mx
        return mx
