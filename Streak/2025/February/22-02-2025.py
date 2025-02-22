class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
        def dfs(depth):
            nonlocal i
            if i == len(traversal):
                return None
            j = i
            while traversal[i] == '-':
                i += 1
            if depth > i - j: # The depth of the current node is greater than that read from traversal
                i = j  # Restore the traversal index and exit
                return None
            val = 0
            while i < len(traversal) and traversal[i] != '-':
                val = val * 10 + int(traversal[i])
                i += 1
            node = TreeNode(val)
            node.left = dfs(depth+1)
            node.right = dfs(depth+1)
            return node

        i = 0
        return dfs(0
