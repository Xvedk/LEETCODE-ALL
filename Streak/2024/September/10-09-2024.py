class Solution:
    def insertGreatestCommonDivisors(self, h: Optional[ListNode]) -> Optional[ListNode]:
        return (f:=lambda n:(q:=n.next) and ListNode(n.val,ListNode(gcd(n.val,q.val),f(q))) or n)(h)
