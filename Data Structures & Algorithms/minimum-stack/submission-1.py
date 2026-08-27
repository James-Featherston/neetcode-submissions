class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minVal = 0
        if len(self.stack) == 0:
            minVal = val
        else:
            minVal = min(val, self.stack[-1][1])
        self.stack.append((val, minVal))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
        
