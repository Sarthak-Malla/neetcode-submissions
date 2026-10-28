class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoDecStack = []
        n = len(temperatures)

        res = [0] * n
        for i in range(n - 1, -1, -1):
            while monoDecStack and monoDecStack[-1][0] <= temperatures[i]:
                monoDecStack.pop()
            
            if monoDecStack and monoDecStack[-1][1] != i:
                res[i] = monoDecStack[-1][1] - i

            monoDecStack.append([temperatures[i], i])

        return res