class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        df = {}

        for i, num in enumerate(nums):
            if target - num in df:
                return [df[target - num], i]
            df[num] = i
        
        return []