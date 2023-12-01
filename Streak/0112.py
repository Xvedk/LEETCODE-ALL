class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        p2, i2 = 0, 0

        for part in word1:
            for letter in part:
                if i2 >= len(word2[p2]):
                    i2 = 0
                    p2 += 1
                if p2 >= len(word2):
                    return False
                if letter != word2[p2][i2]:
                    return False
                i2 += 1
        # check if the pointer on the last part of the second word and we've already checked last letter in this part
        if p2 == len(word2) - 1 and i2 >= len(word2[p2]):
            return True

        return False
        
