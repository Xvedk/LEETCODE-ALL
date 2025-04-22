class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        totalIdeal = 0
        comb = [1]
        dpPrev = [1] * (maxValue + 1)
        
        divisors = [[] for _ in range(maxValue + 1)]
        for divisor in range(1, maxValue + 1):
            for multiple in range(divisor, maxValue + 1, divisor):
                divisors[multiple].append(divisor)
        
        
        for chainLength in range(1, n + 1):
            sumChains = sum(dpPrev[1:]) % MOD
            
            choose_i = chainLength - 1
            if choose_i >= len(comb):
                numerator = (n - 1) - (choose_i - 1)
                denominator = choose_i
                invDen = pow(denominator, MOD - 2, MOD)
                nextComb = comb[choose_i - 1] * numerator % MOD * invDen % MOD
                comb.append(nextComb)
            
            totalIdeal = (totalIdeal + sumChains * comb[choose_i]) % MOD
            
            if chainLength == n:
                break
            
            dpCurr = [0] * (maxValue + 1)
            nonzero_total = 0
            for val in range(1, maxValue + 1):
                s = 0
                for d in divisors[val]:
                    if d < val:
                        s += dpPrev[d]
                dpCurr[val] = s % MOD
                nonzero_total += dpCurr[val]
            
            if nonzero_total == 0:
                break
            
            dpPrev = dpCurr
        
        return totalIdeal        
