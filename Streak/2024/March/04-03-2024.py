class queue(object):
    def __init__(self,array: List[int]) -> None:
        self.array = array
        return None
    def popend(self) -> int:
        x = self.array[-1]
        del self.array[-1]
        return x
    def popleft(self) -> int:
        x = self.array[0]
        del self.array[0]
        return x
    def state(self) -> bool:
        return bool(len(self.array) >= 1)
    def index(self,index: int) -> int:
        return self.array[index]

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        maps = queue(sorted(tokens))
        score = int(0)
        maxs = int(0)
        while maps.state() == True:
            # Face Up
            if power >= maps.index(0):
                t = maps.popleft()
                power -= t
                score += 1
                maxs = max(score,maxs)
            # Face Down
            elif score >= 1:
                t = maps.popend()
                power += t
                score -= 1
            # End
            else:
                break
        return maxs 
