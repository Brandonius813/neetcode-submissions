class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # 3-Striped Flag Algorithm.  Pointer at left/right of array, pointer that moves through array left to right.  If moving pointer is a 0, swap w/left, iterate left and center.  If moving pointer is a 2, swap w/right, only iterate right.  End when center pointer is past the right pointer.

        def swap(L, R):
            tmp = nums[L]
            nums[L] = nums[R]
            nums[R] = tmp

        l, r, i = 0, len(nums) - 1, 0

        while i <= r:

            if nums[i] == 0:
                swap(i, l)
                l += 1

            if nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
        
            i += 1
