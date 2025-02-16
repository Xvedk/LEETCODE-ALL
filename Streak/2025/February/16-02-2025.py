class Solution:

    def constructDistancedSequence(self, n: int) -> List[int]:
        arr = [0] * (2 * n - 1)  # Create result array of required size
        used = [False] * (n + 1)  # Track used numbers
        self.solve(n, arr, used, 0)
        return arr

    def solve(self, n, arr, used, index):
        if index == len(arr):  # If all positions are filled, return True
            return True
        
        if arr[index] != 0:  # Skip filled positions
            return self.solve(n, arr, used, index + 1)

        for num in range(n, 0, -1):  # Try placing largest number first
            if used[num]:
                continue
            
            if num == 1:
                arr[index] = 1
                used[num] = True
                if self.solve(n, arr, used, index + 1):
                    return True
                arr[index] = 0
                used[num] = False
            else:
                next_index = index + num
                if next_index < len(arr) and arr[next_index] == 0:
                    arr[index], arr[next_index] = num, num
                    used[num] = True
                    if self.solve(n, arr, used, index + 1):
                        return True
                    arr[index], arr[next_index] = 0, 0
                    used[num] = False
        
        return False
