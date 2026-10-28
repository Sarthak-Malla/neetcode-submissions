class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op, cl = ['(', '{', '['], [')', '}', ']']

        for c in s:
            if c in cl:
                if not len(stack) or stack[-1] != op[cl.index(c)]:
                    return False
                
                if stack[-1] == op[cl.index(c)]:
                    stack.pop()
                    continue

            stack.append(c)
        
        return len(stack) == 0