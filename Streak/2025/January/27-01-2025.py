class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        m=[[False]*numCourses for _ in range(numCourses)]
        
        for u,v in prerequisites:
            m[u][v]=True
            
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    m[i][j]|=m[i][k] and m[k][j]
                    
        ans=[]
        for u,v in queries:
            ans.append(m[u][v])
            
        return ans    
