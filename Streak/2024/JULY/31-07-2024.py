class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_wdth: int) -> int:

        @lru_cache(None)
        def dfs(i: int, wdth: int, hght: int)-> int:

            if i == len(books): return 0

            bookwdth, bookhght = books[i]
            wdth+= bookwdth
            ans = inf

            if wdth <= shelf_wdth:

                if bookhght <= hght:
                    ans = dfs(i+1, wdth,  hght)
                else:
                    ans = min(ans, bookhght - hght + dfs(i+1, wdth,  bookhght))

            return min(ans, bookhght + dfs(i+1, bookwdth, bookhght))


        return dfs(0, 0, 0)
