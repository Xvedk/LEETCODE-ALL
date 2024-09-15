class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowelCount = 0
        start = defaultdict(int)
        start[0] = -1
        end = defaultdict(int)
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        maxi = 0

        for idx, letter in enumerate(s):
            if letter in vowels:
                vowelCount ^= (1 << vowels[letter])
            if vowelCount not in start:
                start[vowelCount] = idx
            end[vowelCount] = idx
        
        for key, val in end.items():
            if key != 0:
                maxi = max(maxi, val - start[key])
            else:
                maxi = max(maxi, val - start[key])


        return maxi


        
        
