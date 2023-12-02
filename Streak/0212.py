class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        freq = {}
        for i in chars:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        count = 0

        for word in words:
            temp, flag = freq.copy(), True
            for letter in word:
                if letter in temp:
                    if temp[letter]==0:
                        flag = False
                        break
                    temp[letter]-=1
                else: 
                    flag = False
                    break
            if flag:
                count+=len(word)

        return count
