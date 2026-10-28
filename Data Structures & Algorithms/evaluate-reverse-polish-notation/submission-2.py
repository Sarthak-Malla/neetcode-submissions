class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def getAns(n1: int, n2: int, t: str) -> int:
            if t == "+":
                return n1 + n2
            elif t == "-":
                return n2 - n1
            elif t == "*":
                return n1 * n2
            elif t == "/":
                return int(n2 / n1)

        numStack = []

        for t in tokens:
            if t.isnumeric() or (t.startswith('-') and t[1:].isnumeric()):
                numStack.append(int(t))
            else:
                num1 = numStack.pop()
                num2 = numStack.pop()
                numStack.append(getAns(num1, num2, t))
        
        return numStack[-1]