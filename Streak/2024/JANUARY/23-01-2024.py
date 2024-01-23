class Solution:
    def maxLength(self, arr: List[str]) -> int:

        def get_bitmap(arr) -> Dict[int, int]:
            bitmap = defaultdict(int)
            bitmap[0] = 0

            def make(word):
                ret = 0
                for ch in word:
                    ret |= 1 << (ord(ch) - ord('a'))
                return ret

            def dfs(curr_bitmap, index, curr_length):
                bitmap[curr_bitmap] = max(bitmap[curr_bitmap], curr_length)
                if index == len(arr):
                    return

                bmap = make(arr[index])
                if curr_bitmap & bmap == 0:
                    dfs(curr_bitmap | bmap, index+1, curr_length + len(arr[index]))

                dfs(curr_bitmap, index+1, curr_length)
            
            dfs(0, 0, 0)
            return bitmap

        arr = [word for word in arr if len(word) == len(set(word))]
        if len(arr) == 1:
            return len(arr[0])
        
        n = len(arr)
        left, right = arr[:n//2], arr[n//2:]

        left, right = get_bitmap(left), get_bitmap(right)       # dictionaries
        ans = 0

        for l in left:
            for r in right:
                if l & r == 0:
                    ans = max(ans, left[l] + right[r])

        return ans
