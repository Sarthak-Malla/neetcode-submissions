class MinStack:

    def __init__(self):
        self.minStack = []
        self.currMin = None

    def push(self, val: int) -> None:
        if self.currMin is None or self.currMin > val:
            self.currMin = val
        self.minStack.append((val, self.currMin))

    def pop(self) -> None:
        self.minStack.pop()
        self.currMin = self.minStack[-1][1] if self.minStack else None

    def top(self) -> int:
        return self.minStack[-1][0]

    def getMin(self) -> int:
        return self.minStack[-1][1]
