class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(nums, left, right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if right <= left:
                return -1
            
            if target < nums[mid]:
                return binary(nums, left, mid - 1)
            elif target > nums[mid]:
                return binary(nums, mid + 1, right)
        
        return binary(nums, 0, len(nums) - 1)