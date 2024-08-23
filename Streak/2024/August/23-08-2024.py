class Solution:
    def fractionAddition(self, expression: str) -> str:
        n1, d1 = 0, 1  # Initialize the first fraction as 0/1
        i, n = 0, len(expression)
        while i < n:
            # Determine if the current fraction is negative
            negative = expression[i] == '-'
            if expression[i] in '+-': i += 1
            # Parse the numerator
            n2, d2 = 0, 0
            while i < n and expression[i].isdigit():
                n2 = n2 * 10 + int(expression[i])
                i += 1
            # Skip the '/' character
            if i < n and expression[i] == '/': i += 1
            # Parse the denominator
            while i < n and expression[i].isdigit():
                d2 = d2 * 10 + int(expression[i])
                i += 1
            # Apply the sign to the numerator
            if negative: n2 = -n2
            # Calculate the result fraction
            n1, d1 = self.calculate(n1, d1, n2, d2)
        return f"{n1}/{d1}"
    
    def gcd(self, a: int, b: int) -> int:
        return abs(a) if b == 0 else self.gcd(b, a % b)
    
    def lcm(self, a: int, b: int) -> int:
        return abs(a * b) // self.gcd(a, b)
    
    def reduce(self, numerator: int, denominator: int) -> tuple[int, int]:
        GCD = self.gcd(numerator, denominator)
        return numerator // GCD, denominator // GCD
    
    def calculate(self, n1: int, d1: int, n2: int, d2: int) -> tuple[int, int]:
        lcmDenominator = self.lcm(d1, d2)
        adjustedNum1 = n1 * (lcmDenominator // d1)
        adjustedNum2 = n2 * (lcmDenominator // d2)

        numerator = adjustedNum1 + adjustedNum2
        denominator = lcmDenominator

        return self.reduce(numerator, denominator)
