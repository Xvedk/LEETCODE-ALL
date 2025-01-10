class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        s1 = set(words1)
        char = {}
        for word in words2:
            for j in word:
                c = word.count(j)
                if j not in char or c > char[j]:
                    char[j] = c
        for word in words1:
            for j in char:
                if word.count(j) < char[j]:
                    s1.remove(word)
                    break
        return list(s1)


