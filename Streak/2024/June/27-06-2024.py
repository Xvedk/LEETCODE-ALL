class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge1, edge2 = edges[:2]
        return [element for element in edge1 if element in edge2][0]
#if you upvote you will hear good news inn 10 mins (those who are waiting for a job will get job offer in a week)
