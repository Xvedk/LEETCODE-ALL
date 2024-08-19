class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def f(n):
            if n==1: return 0
            sqrtn=int(sqrt(n))
            isPrime=True
            factor=1
            for i in range(2, sqrtn+1):
                if n%i==0:
                    factor=i
                    isPrime=False
                    break
            return n if isPrime else f(factor)+f(n//factor)
        return f(n)
        
