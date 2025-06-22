class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        for i in range(0,len(s),k):
            ans += [s[i:i+k]]
        #     print(i)
        # print(len(ans[-1]) < k)
        # print(len(ans[-1]))
        if len(ans[-1]) < k:
            ans[-1]=ans[-1]+fill*(k-len(ans[-1]))
            # print(ans[-1])
        return ans
