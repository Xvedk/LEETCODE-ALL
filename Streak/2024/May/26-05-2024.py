class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        f0, f1 = 1, 0 # f(0, 0), f(0, 1) respectively
        s0, s1 = 2, 1 # f(1, 0), f(1, 1) respectively
        t0, t1 = 4, 4 # f(2, 0), f(2, 1) respectively

        if n == 1:
            return s0 + s1
        elif n == 2:
            return t0 + t1
        
        for i in range(3, n + 1):
            r0 = (f0 + s0 + t0) % MOD # f(i, 0)
            r1 = (f0 + f1 + s0 + s1 + t0 + t1) % MOD # f(i, 1)

            # update f(i-3), f(i-2), f(i-1)
            f0, f1 = s0, s1 
            s0, s1 = t0, t1
            t0, t1 = r0, r1
         
        return (t0 + t1) % MOD # f(n) = f(n, 0) + f(n, 1)
