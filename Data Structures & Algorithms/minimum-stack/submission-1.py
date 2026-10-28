class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float("infinity")

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(self.minimum, val)

    def pop(self) -> None:
        top = self.stack.pop()
        if top == self.minimum:
            if self.stack:
                self.minimum = min(self.stack)
            else:
                self.minimum = float("infinity")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
