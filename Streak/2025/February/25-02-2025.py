class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ps = [0]

        for i in arr:
            ps.append(ps[-1] + i)
        
        count = 0
        num_even = 1
        num_odd = 0
        MOD = 10**9 + 7
        for i in range(1, len(arr)+1):
            curr = ps[i]
            if curr%2 == 1:
                count += num_even%MOD
                num_odd+=1
            else:
                count+= num_odd%MOD
                num_even+=1
        return count%MOD
