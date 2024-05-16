class Solution:
    def evaluateTree(self, root: TreeNode) -> bool:
        if root.val == 0:   # False Leaf
            return False
        elif root.val == 1:   # True Leaf
            return True
        elif root.val == 2: # OR node
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        elif root.val == 3: # AND node
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
