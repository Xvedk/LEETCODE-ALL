class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        move_horizontal_vertical = [-1, 0, 1]

        m = len(img)
        n = len(img[0])

        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                cnt = 0
                val = 0

                for a in move_horizontal_vertical:
                    for b in move_horizontal_vertical:
                        x = i + a
                        y = j + b

                        if x < 0 or x >= m or y < 0 or y >= n:
                            continue

                        cnt += 1
                        val += img[x][y]

                res[i][j] = val // cnt

        return res
        
