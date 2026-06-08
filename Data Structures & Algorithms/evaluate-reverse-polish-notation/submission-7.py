class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+","-","/","*"])

        for token in tokens:
            if token not in operators:
                # It's a number (i.e - operand)
                stack.append(token)
            else:
                if not stack:
                    return -1 # not enough operands, invalid expr
                rightOperand = int(stack.pop())
                leftOperand = int(stack.pop())
                if token == "+":
                    result = leftOperand + rightOperand
                    stack.append(result)
                elif token == "-":
                    result = leftOperand - rightOperand
                    stack.append(result)
                elif token == "*":
                    result = leftOperand * rightOperand
                    stack.append(result)
                elif token == "/":
                    result = leftOperand / rightOperand
                    stack.append(int(result))
        
        return int(stack.pop())