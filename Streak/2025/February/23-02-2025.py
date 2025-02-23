# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        if n == 0:
            return None
        node = TreeNode(preorder[0])
        if n == 1:
            return node
        left_size = postorder.index(preorder[1]) + 1
        node.left = self.constructFromPrePost(preorder[1:1+left_size], postorder[:left_size])
        node.right = self.constructFromPrePost(preorder[1+left_size:], postorder[left_size:n-1])
        return node
