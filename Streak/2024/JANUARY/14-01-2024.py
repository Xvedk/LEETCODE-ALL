class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
       
        char1 = [0] * 26
        char2 = [0] * 26

        for ch in word1:
            char1[ord(ch) - ord('a')] += 1

        for ch in word2:
            char2[ord(ch) - ord('a')] += 1

        for i in range(26):
            if (char1[i] == 0 and char2[i] != 0) or (char1[i] != 0 and char2[i] == 0):
                return False

        char1.sort()
        char2.sort()

        return char1 == char2
