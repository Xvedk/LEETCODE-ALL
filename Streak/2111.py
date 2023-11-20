class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        p = 0
        g = 0
        M = 0
        pv = 0
        pg = 0
        pm = 0
        for i in range(len(garbage)-1,-1,-1):
            a = garbage[i].count("P")
            if a != 0:
                 p += a
                 pv = 1
            b = garbage[i].count("G")
            if b != 0:
                g += b
                pg = 1
            c = garbage[i].count("M")
            if c != 0:
                M += c
                pm = 1
            p += travel[i-1] if (i > 0 and pv == 1) else 0
            g += travel[i-1] if (i > 0 and pg == 1) else 0
            M += travel[i-1] if (i > 0 and pm == 1) else 0
        return p + g + M
