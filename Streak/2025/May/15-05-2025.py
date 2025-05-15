class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        return [words[i] for i in range(len(groups)) if i == 0 or groups[i] != groups[i - 1]]
