class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.inorderr = []
        def inorder(root):
            if not root: return
            self.inorderr.append(root.val)
            inorder(root.left)
            inorder(root.right)
        inorder(root)        
        freq = collections.Counter(self.inorderr)
        maxx = max(freq.values())
        return [x for x in freq if freq[x] == maxx]
