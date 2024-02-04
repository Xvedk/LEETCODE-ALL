class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def get_next(index):
            index += 1
            while index < len(s) and s[index] not in td:
                index += 1
            return index

        BIG = 1_000_000
        td, ts = {}, set(t)
        for ch in t:
            td[ch] = td.get(ch, 0) + 1

        ans = (-1, BIG)

        r, l = -1, get_next(-1)

        while True:
            while ts:
                r = get_next(r)
                if r == len(s):
                    break
                ch = s[r]
                td[ch]  -=  1
                if td[ch] == 0:
                    ts.remove(ch)
            else:
                if r - l < ans[1] - ans[0]:
                    ans = (l, r)

                ch = s[l]
                td[ch]  +=  1
                if td[ch] == 1:
                    ts.add(ch)
                l = get_next(l)
                continue              # if no break above
            break                     # if break in `while ts` cycle

        return s[ans[0]: ans[1] + 1] if ans[1] < BIG else ''
