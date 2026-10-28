class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if n < 2:
            return nums
        
        if k > n:
            return [max(nums)]
        
        res = []

        for l in range(0, n - k + 1):
            res.append(max(nums[l:l+k]))
            
        return res