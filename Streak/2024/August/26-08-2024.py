class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack = [root]
        output = []
        
        while stack:
            node = stack.pop()
            output.append(node.val)
            # Add children to stack if they exist
            if node.children:
                stack.extend(node.children)
        
        # Since the nodes were added in root-first order, we reverse the output for postorder
        return output[::-1]
