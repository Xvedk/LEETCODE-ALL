class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []  # Stack to hold characters and operators
        
        # Iterate over each character in the expression
        for c in expression:
            if c != ')' and c != ',': 
                stk.append(c)  # Push valid characters to the stack
            elif c == ')':  # When ')' is encountered, evaluate subexpression
                exp = []  # List to hold boolean values of the current subexpression
                
                # Pop characters until '(' is found, collect 't' or 'f' values
                while stk and stk[-1] != '(':
                    t = stk.pop()
                    exp.append(True if t == 't' else False)
                
                stk.pop()  # Pop the '(' from the stack
                
                if stk:
                    t = stk.pop()  # Get the operator before '('
                    v = exp[0]  # Initialize result with the first value
                    
                    # Perform the corresponding logical operation
                    if t == '&':  # AND operation
                        for b in exp:
                            v &= b
                    elif t == '|':  # OR operation
                        for b in exp:
                            v |= b
                    else:  # NOT operation
                        v = not v
                    
                    # Push the result back to the stack as 't' or 'f'
                    stk.append('t' if v else 'f')
        
        # Return the final result from the stack
        return stk[-1] == 't'
