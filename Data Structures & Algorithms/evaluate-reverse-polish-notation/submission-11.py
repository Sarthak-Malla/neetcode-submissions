class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                st.append(int(token))
                continue

            b = st.pop()
            a = st.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            else:
                result = int(a / b)  # truncate toward zero

            st.append(result)

        return st[-1]