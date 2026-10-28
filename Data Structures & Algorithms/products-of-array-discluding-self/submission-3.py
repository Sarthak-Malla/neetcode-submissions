class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        
        res = []
        for i in range(n):
            if i == 0:
                res.append(suffix[i + 1])
            else:
                if i + 1 < n:
                    res.append(prefix[i - 1] * suffix[i + 1])
                else:
                    res.append(prefix[i - 1])

        return res