class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if nums[0] > 0 or nums[n - 1] < 0:
            return []
        
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i+1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    inner = [nums[i], nums[j], nums[k]]
                    res.append(inner)
                    j, k = j + 1, k - 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
            
        return res