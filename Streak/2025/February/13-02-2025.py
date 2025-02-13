class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()  
        temp = []    
        i, j, ops = 0, 0, 0 

        while len(nums) - i + len(temp) - j >= 2:
            if i < len(nums):
                first = nums[i]
                if j < len(temp) and temp[j] < first:
                    first = temp[j]
                    j += 1
                else:
                    i += 1
            else:
                first = temp[j]
                j += 1

            if first >= k:
                break  

            if i < len(nums):
                second = nums[i]
                if j < len(temp) and temp[j] < second:
                    second = temp[j]
                    j += 1
                else:
                    i += 1
            else:
                second = temp[j]
                j += 1

            temp.append((min(first, second) * 2) + max(first, second))
            ops += 1
        
        return ops
