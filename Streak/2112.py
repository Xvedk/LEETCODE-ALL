from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Sort the points based on x-coordinates
        points.sort(key=lambda point: point[0])

        # Calculate the maximum width
        max_width = 0
        for i in range(1, len(points)):
            max_width = max(max_width, points[i][0] - points[i - 1][0])

        return max_width
