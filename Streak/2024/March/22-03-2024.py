class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Edge case: Empty linked list or single node
        if not head or not head.next:
            return True
        
        # Find the middle of the linked list using fast and slow pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Compare the first half of the original list with the reversed second half
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
        
