#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        #check all the corresponding downward values and return true if they are the same
        def comparison(root, head):
            if head is None: return True
            if root is None: return False
            if root.val != head.val: return False

            return comparison(root.left, head.next) or comparison(root.right, head.next)
        
        #traverse all nodes in tree to check if the node value is equal to list's head
        def inOrder(root, head):
            if root is None: return
            res = False
            #if the values are equal, then check the next values
            if root.val == head.val:
                res = comparison(root, head)

            if res == True: return True
            return inOrder(root.left, head) or inOrder(root.right, head)

        return inOrder(root, head)
