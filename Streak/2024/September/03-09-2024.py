class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res=""
        for  i in s:
            res+=str(ord(i)-96)
        while(k>0 and len(res)>1):
            temp=0
            i=0
            while(i<len(res)):
                temp+=int(res[i])
                i+=1
            res=str(temp)
            k-=1
        return int(res)
        
