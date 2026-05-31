class Solution:
    def isValid(self, s: str) -> bool:
        bracketsMap = {'}':'{',']':'[',')':'('}
        stack = []
        for bracket in s:
            if bracket in ['{','(','[']:
                stack.append(bracket)
            else:
                if not stack or stack[-1] != bracketsMap[bracket]:
                    return False
                stack.pop()
            
        if len(stack) == 0:
            return True
        else: 
            return False