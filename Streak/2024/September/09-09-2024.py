class Solution:
    def spiralMatrix(self, m: int, n: int, 
                           head: ListNode) -> List[List[int]]:

        ans = [[-1] * n for _ in range(m)]
        ans[0][0], head = head.val, head.next
        r, c, dr, dc, R, C = 0, 0, 0, 1, range(m), range(n)

        while head:
            if r+dr in R and c+dc in C and ans[r+dr][c+dc] == -1:
                r+= dr ;  c+= dc 
                ans[r][c], head = head.val, head.next
            else:                               
                dr, dc = dc, -dr
                
        return ans
