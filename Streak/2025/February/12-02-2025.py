class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(i):
            s = 0
            while(i):
                s += i%10
                i //= 10
            return s
        pairs = []
        for n in nums:
            s = digit_sum(n)
            pairs.append((s,n))
        pairs.sort()
        max_sum = -1
        for i in range(1,len(nums)):
            if pairs[i][0] == pairs[i-1][0]:
                cur_sum = pairs[i][1]+pairs[i-1][1]
                max_sum = max(max_sum, cur_sum)
        return max_sum     
