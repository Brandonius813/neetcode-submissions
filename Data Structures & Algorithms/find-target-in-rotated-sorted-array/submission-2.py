# Had 2 typos, fixed those.
# Missed the edge case where the array doesn't have a pivot and is fully sorted.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
       
       # Deal with edge cases where t is at the start or end of array
        if target == nums[0]:
            return 0
        
        if target == nums[-1]:
            return len(nums) - 1
        
        # Find Pivot
        l = 0
        r = len(nums) - 1

        while l < r: #This will end with l and r sitting on the pivot point - the minimum value of the right array
            m = (l+r) // 2

            if nums[m] < nums[r]:
                r = m
            
            else:
                l = m + 1

         # Are we looking for left or right sorted array?
        if r == l == 0: #Whole array is sorted - reset
            r = len(nums) - 1

        elif target < nums[0] and target < nums[-1]: #Go right
            r = len(nums) - 1
        
        else: #Go left
            l = 0
            r -= 1

        # Search within sorted sub-array for target
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] > target:
                r = m - 1
            
            if nums[m] < target:
                l = m + 1
        
        return -1