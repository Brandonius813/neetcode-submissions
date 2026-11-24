class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        nums.sort()

        for i in range(len(nums)):
            if i == 0:
                continue
            
            if nums[i] == nums[i-1] + 1:
                continue
            
            else:
                return False
        
        return True
            

            

