class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # Iterate through the array, stopping at the third-to-last element
        for i in range(len(arr) - 2):
            # Check if the current element and the next two elements are all odd
            if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
                return True
        return False
