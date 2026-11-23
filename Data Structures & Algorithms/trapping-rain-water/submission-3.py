class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        right = [0] * n
        left = [0] * n
        curr_max = 0

        for i in range(n - 1, -1, -1):
            if height[i] <= curr_max:
                right[i] = curr_max
            curr_max = max(height[i], curr_max)
        
        curr_max = 0
        for i in range(n):
            if height[i] <= curr_max:
                left[i] = curr_max
            
            curr_max = max(height[i], curr_max)

        water = 0
        for i in range(n):
            curr_water = max(0, min(left[i], right[i]) - height[i])
            water += curr_water

        return water