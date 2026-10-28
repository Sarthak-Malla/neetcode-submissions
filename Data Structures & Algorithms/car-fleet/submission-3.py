class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        state = [[p, s] for p, s in zip(position, speed)]
        state = sorted(state)[::-1]

        stack = []
        for p, s in state:
            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()    
        
        return len(stack)
