class Solution:
    def getMaxArr(self, n, height):
        maxLeft = [height[0]]
        curr = maxLeft[-1]
        for i in range(1, n):
            if i - 1 >= 0:
                maxLeft.append(max(curr, height[i - 1]))
                curr = max(curr, height[i])
        return maxLeft
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = self.getMaxArr(n, height)
        maxRight = self.getMaxArr(n, height[::-1])[::-1]

        res = 0
        for i in range(n):
            if maxLeft[i] == 0 or maxRight == 0:
                continue
            
            water = min(maxLeft[i], maxRight[i]) - height[i]
            res += water if water > 0 else 0

        return res