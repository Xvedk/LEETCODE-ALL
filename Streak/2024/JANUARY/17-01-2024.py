class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        has = {}
        for i in arr: #create hashmap with frequency of every number
            if i in has:
                has[i]+=1
            else:
                has[i]=1

        valuehash = {}
        
        for key,val in has.items(): 
            if val in valuehash:  #storing the count of frequencies
                valuehash[val]+=1 
            else:
                valuehash[val]=1

        for i in valuehash:  #if count of any frequency>1, return False
            if valuehash[i]>1:
                return False
        return True
        
