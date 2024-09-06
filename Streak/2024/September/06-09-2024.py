class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        set_nums = set(nums)

        def helper(node):
            if not node:
                return None
            node.next = helper(node.next)
            if node.val in set_nums:
                return node.next
            return node

        return helper(head)
