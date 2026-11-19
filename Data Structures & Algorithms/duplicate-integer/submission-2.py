class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        shortened = set(nums)

        if len(shortened) == len(nums):
            return False
        
        else:
            return True