class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(["+", "-", "*", "/"])
        st = []
        
        for token in tokens:
            if token not in ops:
                st.append(token)
                continue
            
            a = int(st.pop())
            b = int(st.pop())

            if token == "+":
                st.append(str(a + b))
            elif token == "-":
                st.append(str(b - a))
            elif token == "*":
                st.append(str(a * b))
            else:
                div = b // a if b // a >= 0 or b % a == 0 else b // a + 1
                st.append(str(div))
        
        return int(st[-1])