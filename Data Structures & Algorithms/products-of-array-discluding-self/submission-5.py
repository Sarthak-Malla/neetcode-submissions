class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [nums[-1]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i])
        
        for i in range(1, len(nums)):
            suffix.append(suffix[i - 1] * nums[-1 * (i + 1)])
        
        suffix = suffix[::-1]
        
        res = []
        for i in range(len(nums)):
            left = prefix[i - 1] if i - 1 >= 0 else 1
            right = suffix[i + 1] if i + 1 < len(nums) else 1

            res.append(left * right)
        
        return res
