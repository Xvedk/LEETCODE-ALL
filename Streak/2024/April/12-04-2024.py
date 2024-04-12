class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        ans=0
        st=[]
        for r, x in enumerate(height):
            while st and height[st[-1]]<x:
                m=st[-1]
                st.pop()
                if not st: break
                l=st[-1]
                h=min(x, height[l])-height[m]
                w=r-l-1
                ans+=h*w
            st.append(r)
        return ans
        
