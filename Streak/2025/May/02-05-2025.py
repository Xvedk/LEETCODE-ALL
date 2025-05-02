class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        right = -1
        temp = []
        result = []
        
        for i in range(len(dominoes)):
            value = dominoes[i]
            if value == ".":
                temp.append(value)
                continue
            if value == "L":
                if right == -1:
                    result += (len(temp) + 1) * ["L"]
                else:
                    length = i - right + 1
                    if length % 2 == 0:
                        result += (length // 2) * ["R"]
                        result += (length // 2) * ["L"]
                    else:
                        result += (length // 2) * ["R"]
                        result += ["."]
                        result += (length // 2) * ["L"]
                    right = -1
                temp = []
            if value == "R":
                if right == -1:
                    right = i
                    result += temp
                else:
                    result += (i - right) * ["R"]
                    right = i
                temp = []

        if temp or right != -1:
            if right != -1:
                result += (len(temp) + 1) * ["R"]
            else:
                result += temp
                
        return "".join(result)
