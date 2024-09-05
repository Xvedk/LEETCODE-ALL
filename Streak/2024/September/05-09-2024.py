class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        req_sum = mean * (len(rolls) + n) - sum(rolls)
        if (6*n < req_sum or n > req_sum):
            return []
       
        op = []
        for i in range(n-1, -1, -1):
            curr = req_sum // (i+1)
            req_sum -= curr
            op.append(curr)
        return op
