class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = dict()
        n = len(nums)

        for i in range(n):
            comp = target - nums[i]
            if comp in complements:
                return [complements[comp], i]
            complements[nums[i]] = i
        
        return [0, 1]
    