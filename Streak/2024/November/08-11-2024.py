class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n=len(nums)
        pre=[]
        mask=(1<<maximumBit)-1
        for x in nums:
            pre.append(mask^x)
            mask=mask^x
        pre.reverse()
        return pre
