from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        left = [0] * n
        right = [0] * n

        # Calculate the previous smaller element for each element in the array
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        # Calculate the next smaller element for each element in the array
        for i in range(n - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        result = 0

        # Calculate the contribution of each element to the final result
        for i in range(n):
            result = (result + arr[i] * (i - left[i]) * (right[i] - i)) % MOD

        return result


