class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def ham(w1,w2):
            temp = 0
            for x,y in zip(w1,w2):
                if x!=y:
                    temp += 1
            return temp == 1

        dp = [1 for x in range(len(words))]
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if len(words[i]) == len(words[j]) and ham(words[i],words[j]) and groups[i]!=groups[j]:
                    dp[j] = max(dp[j],dp[i]+1)
        
        m = max(dp)
        req_len = -1
        ans = []
        for i in range(len(dp)):
            if dp[i] == m:
                req = len(words[i])
                ans.append(i)
                m-=1
                break
        for i in range(len(dp)-1,-1,-1):
            if dp[i] == m and len(words[i]) == req and ham(words[ans[-1]],words[i]) and groups[ans[-1]] != groups[i]:
                ans.append(i)
                m-=1
        return [words[i] for i in ans][::-1]
