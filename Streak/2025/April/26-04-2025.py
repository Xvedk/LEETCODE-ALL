class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        leftBound = -1
        lastMin = -1
        lastMax = -1
        
        # Iterate through the array
        for i in range(len(nums)):
            # If current number is out of range, update the left bound
            if nums[i] < minK or nums[i] > maxK:
                leftBound = i
            
            # Update the positions of minK and maxK
            if nums[i] == minK:
                lastMin = i
            if nums[i] == maxK:
                lastMax = i
            
            # Calculate the count of valid subarrays ending at position i
            # The valid subarrays must contain both minK and maxK
            # And start after the leftBound
            validSubarrays = min(lastMin, lastMax) - leftBound if min(lastMin, lastMax) > leftBound else 0
            result += validSubarrays
        
        return result         
