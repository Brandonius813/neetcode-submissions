class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l, r, t = 0, len(nums)-1, 0

        while t <= r:
            if nums[t] == 0:
                tmp = nums[l]
                nums[l] = nums[t]
                nums[t] = tmp

                l += 1
            
            if nums[t] == 2:
                tmp = nums[r]
                nums[r] = nums[t]
                nums[t] = tmp

                r -= 1
                t -= 1
            
            t += 1
