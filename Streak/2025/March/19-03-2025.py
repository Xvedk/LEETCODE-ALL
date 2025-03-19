class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, i0, op = len(nums), -1, 0
        nums.append(0) # append 0 avoid of try-except
        while True:
            i0 = nums.index(0, i0+1)  # Find next 0
            if i0 >= n-2:  
                break  
            nums[i0+1] ^=1 # Use xor to flip i0+1
            nums[i0+2] ^=1 # Flip i0+2
            op+=1  
        return op if i0>=n else -1  
        
