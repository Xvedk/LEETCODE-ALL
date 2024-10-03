class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # Step 1: Calculate total sum and the remainder that needs to be removed
        total_sum = sum(nums)
        target_remainder = total_sum % p
        
        # If the total sum is already divisible by p, no need to remove anything
        if target_remainder == 0:
            return 0
        
        # Step 2: Initialize variables
        prefix_sum = 0
        min_length = len(nums)
        remainder_map = {0: -1}  # This is used to store the mod value of prefix sums
        
        # Step 3: Traverse the array
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            # Calculate the mod of the required prefix sum to find the subarray
            needed_remainder = (prefix_sum - target_remainder) % p
            
            if needed_remainder in remainder_map:
                min_length = min(min_length, i - remainder_map[needed_remainder])
            
            # Update the map with the current prefix_sum mod p and index
            remainder_map[prefix_sum] = i
        
        # Step 4: If no valid subarray was found, return -1
        return min_length if min_length < len(nums) else -1
