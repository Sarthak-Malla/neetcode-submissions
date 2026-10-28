class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = dict()
        for num in nums:
            if num in hash:
                return True
            hash[num]=1

        return False
        