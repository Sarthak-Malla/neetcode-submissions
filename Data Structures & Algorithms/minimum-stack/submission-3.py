class MinStack:

    def __init__(self):
        self.st = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.minStack or (self.minStack and self.minStack[-1] >= val):
            self.minStack.append(val)
        self.st.append(val)

        print(self.st, self.minStack)

    def pop(self) -> None:
        val = self.st.pop()
        if self.minStack[-1] == val:
            self.minStack.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
