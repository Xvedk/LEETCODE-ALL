class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        # Dictionary to map operators to corresponding functions
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y),  # Truncates towards zero for integer division
        }

        for token in tokens:
            if token in operators:
                # Perform operation for operators
                y = stack.pop()
                x = stack.pop()
                result = operators[token](x, y)
                stack.append(result)
            else:
                # Push operand onto the stack
                stack.append(int(token))

        return stack[0]  # Final result left on the stack
