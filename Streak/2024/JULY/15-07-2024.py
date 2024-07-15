class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = defaultdict(TreeNode)
        hasParent = set()

        for parent, child, isLeft in descriptions:
            if child not in nodes: nodes[child] = TreeNode(child)
            if parent not in nodes: nodes[parent] = TreeNode(parent)
            
            if isLeft: nodes[parent].left = nodes[child]
            else: nodes[parent].right = nodes[child]
            
            hasParent.add(child)
            
        for child in nodes.keys():
            if child not in hasParent:
                return nodes[child]
