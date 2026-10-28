class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front, back = [1], [1]
        n = len(nums)
        for i in range(n):
            front.append(front[i] * nums[i])
            back.append(back[i] * nums[n - 1 - i])
        
        front.pop()
        back.pop()

        res = []
        for i in range(n):
            res.append(front[i] * back[n -1 - i])

        return res