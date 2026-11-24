class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        OB = ['[', '(', '{']
        df = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in OB:
                st.append(c)
                continue

            if not st:
                return False

            if st:
                if st[-1] == df[c]:
                    st.pop()
                else:
                    return False
        
        return len(st) == 0
