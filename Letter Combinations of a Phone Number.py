class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        if not digits:
            return []
        
        result = []
        
        def backtracking(index, combination):
            if index == len(digits):
                result.append(combination)
                return
            
            for letter in keyboard[digits[index]]:
                backtracking(index + 1, combination + letter)
        
        backtracking(0, "")
        return result
