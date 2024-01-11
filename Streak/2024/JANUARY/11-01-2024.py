class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        INF=10**10
        def go(node,mn,mx):
            ans=0
            ans=max(ans,node.val-mn)
            ans=max(ans,mx-node.val)
            if node.left:
                ans=max(ans,go(node.left,min(mn,node.val),max(mx,node.val)))
            if node.right:
                ans=max(ans,go(node.right,min(mn,node.val),max(mx,node.val)))
            return ans
        return go(root,INF,-INF)
