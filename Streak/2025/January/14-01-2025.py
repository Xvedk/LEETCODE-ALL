class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = [0]*len(A)
        seen = set()
        count= 0

        for i in range(len(A)):
            if A[i] in seen:
                count+=1
            seen.add(A[i])
            if B[i] in seen:
                count+=1
            seen.add(B[i])

            C[i] = count
        
        return C
