class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Convert strings to sorted lists of characters
        ss = sorted(s)
        tt = sorted(t)

        # Check if the sorted lists are equal
        return ss == tt
