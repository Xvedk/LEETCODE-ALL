class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n=len(mat[0])
        m=len(mat)
        c=0
        trans=[[k[i] for k in mat] for i in range(n)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1 and 1 not in mat[i][:j]+mat[i][j+1:] and 1 not in trans[j][:i]+trans[j][i+1:]: c+=1
        return c
