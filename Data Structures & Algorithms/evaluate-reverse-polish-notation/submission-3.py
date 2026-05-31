class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] #Initialize stack

        for token in tokens:
            if token not in ['+', '-', '*','/']: #Token is a number
                stack.append(int(token)) #Push number into stack
            
            elif token in ['+', '-', '*','/']: #If operator
                rightOperand = stack.pop() #Pop last two numbers
                leftOperand = stack.pop()

                if token == '+':
                    total = leftOperand + rightOperand 
                    stack.append(total)
                elif token == '-':
                    total = leftOperand - rightOperand 
                    stack.append(total)
                elif token == '*':
                    total = leftOperand * rightOperand 
                    stack.append(total)
                elif token == '/':
                    total = int(leftOperand / rightOperand)
                    stack.append(total)
        #After loop completes return the result in stack
        return stack.pop()
