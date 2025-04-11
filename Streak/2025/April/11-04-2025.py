class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for num in range(low,high+1):
            s=str(num)
            if len(s) %2!=0:
                continue
            half=len(s)//2
            frst_sum=sum(int(i) for i in s[:half])
            second_sum=sum(int(i) for i in s[half:])
            if frst_sum==second_sum:
                count+=1
            frst_sum,second_sum=0,0

        return count
