class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = set(["(", "{", "["])
        bracks = {")": "(", "}": "{", "]": "["}

        for i in s:
            if i in op:
                stack.append(i)
                continue
            
            if not stack:
                return False

            t = stack.pop()
            if bracks[i] == t:
                continue
            else:
                return False
        
        return len(stack) == 0
