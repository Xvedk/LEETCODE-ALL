class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        max_letter, indexex = '', []
        length = 0
        for index, letter in enumerate(word):
            if letter > max_letter:
                max_letter = letter
                indexes = [index]
            elif letter == max_letter:
                indexes.append(index)
            length += 1
        
        max_length = length + 1 - numFriends
        res = ''
        for index in indexes:
            res = max(res, word[index: index + max_length])
        return res
