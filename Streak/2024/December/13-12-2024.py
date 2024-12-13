class Solution:
    def findScore(self, nums: List[int]) -> int:
        # Step 1: Prepare to mark elements
        n = len(nums)
        marked = [False] * n  # To keep track of marked elements
        indexed_nums = list(enumerate(nums))  # Pair indices with their values
        
        # Step 2: Sort by value and then by index
        indexed_nums.sort(key=lambda x: (x[1], x[0]))

        score = 0  # Initialize score

        # Step 3: Process the array based on the sorted order
        for idx, value in indexed_nums:
            if not marked[idx]:  # Only process unmarked elements
                score += value  # Add value to the score

                # Mark the current element and its adjacent elements
                marked[idx] = True
                if idx > 0:
                    marked[idx - 1] = True
                if idx < n - 1:
                    marked[idx + 1] = True

        return score
