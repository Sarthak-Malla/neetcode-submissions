class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        front, res = [1] * n, [1] * n
        curr = 1
        for i in range(n):
            front[i] = curr
            curr *= nums[i]
        curr = 1
        for i in range(n-1, -1, -1):
            res[i] = curr * front[i]
            curr *= nums[i]
        return res