class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        prefix = strs[0]
        new_prefix = -1
        for j in range(1, n):
            word = strs[j]
            for i in range(min(len(prefix), len(word))):
                if word[i] != prefix[i]:
                    new_prefix = i
                    break
            if new_prefix != -1:
                prefix = prefix[:new_prefix]
            elif len(prefix) > len(word):
                prefix = word
        
        return prefix
            
