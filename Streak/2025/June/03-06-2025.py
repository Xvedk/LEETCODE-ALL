class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        answer = 0
        box_inv = deque(initialBoxes)
        visited = [0] * len(status)

        while box_inv:
            box = box_inv.popleft()
            if visited[box] == 2:
                continue
            visited[box] += 1
            if status[box] == 1:
                answer += candies[box]
                box_inv.extend(containedBoxes[box])
                for k in keys[box]:
                    status[k] = 1
                visited[box] = 2
            else:
                box_inv.append(box)
            
        return answer
