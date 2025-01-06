class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [1 if box == '1' else 0 for box in list(boxes)]
        move_cnt = 0
        ones_diff = 0
        
        for pos in range(n):
            if answer[pos] == 1:
                ones_diff += 1
                move_cnt += pos

        for pos in range(n):
            if answer[pos] == 1:
                ones_diff -= 2
            answer[pos] = move_cnt
            move_cnt -= ones_diff
        
        
        return answer
