class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {}
        for i, num in enumerate(arr2):
            order[num] = i
        return list(sorted(arr1, key=lambda x: (order.get(x, 1000), x)))
