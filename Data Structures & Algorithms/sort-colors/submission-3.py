class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # I think this is just implement merge sort again?
        # NAHHHH this is Bucket Sort.  We have finite items in the list.
        # Make a hashmap of the values in the list, move through the list and record occurrances, then move through again and overwrite it with the new values.  O(n) and O(1).

        # But, bucket sort is "trivial" - the follow-up wants a 1-pass solution.

        # We could "partition" with a left and right pointer.  Right pointer is "if we find a 0, swap to here" and left pointer is "if we find a 2, swap it to here" - 1s will naturally be leftover in the middle.  (On right swaps, don't increment i - it would put zeroes in the middle)

        # The tricky bit of this algorithm is the right hand swap can't increment i - we could accidentially move i past a 0.

        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1

            elif nums[i] ==2:
                swap(i, r)
                r -= 1
                i -= 1
            
            i += 1
