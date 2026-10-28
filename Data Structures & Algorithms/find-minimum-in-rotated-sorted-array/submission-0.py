class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            if nums[r] > nums[l]:
                break

            m = (l + r) // 2

            if l == m:
                return min(nums[l], nums[r])

            if nums[m] > nums[l]:
                l = m + 1
            elif nums[m] < nums[l]:
                if nums[m] < nums[r]:
                    r = m
                else:
                    l = m + 1
        
        return nums[l]