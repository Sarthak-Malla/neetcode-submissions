class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inverse = {}

        for i in range(len(nums)):
            if inverse.get(nums[i]) != None:
                return [inverse.get(nums[i]), i]
            
            inverse[target - nums[i]] = i
        
        return [0, 1]