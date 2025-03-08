class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n=len(blocks)
        wCnt=0
        for i in range(0, k):
            if blocks[i]=='W':
                wCnt+=1
                
        cnt=wCnt
        for i in range(k, n):
            if blocks[i-k]=='W':
                wCnt-=1
            if blocks[i]=='W':
                wCnt+=1
            cnt=wCnt if wCnt<cnt else cnt
        
        return cnt
