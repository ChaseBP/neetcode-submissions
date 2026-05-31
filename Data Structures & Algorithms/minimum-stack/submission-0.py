class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            minVal = val
            self.stack.append((val,minVal))
        else:
            currMinVal = self.stack[-1][1] #Get the current min
            minVal = currMinVal if currMinVal < val else val #Update the new min value
            #Push to stack
            self.stack.append((val,minVal))

    def pop(self) -> None:
        if not self.stack:
            return None
        else:
            return self.stack.pop()


    def top(self) -> int:
        if not self.stack: 
            return None
        else:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1][1]
