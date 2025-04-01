# TC: O(n)
# SC: O(n)
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        @cache
        def dfs(i):
            # base case
            if i >= n: return 0
            p, b = questions[i]
            # two choices at each step - skip or not skip
            # skip - go to next question
            # not skip - take the point and skip next b questions
            # -> max(skip, not skip)
            return max(dfs(i + 1), p + dfs(i + b + 1))
        return dfs(0)
