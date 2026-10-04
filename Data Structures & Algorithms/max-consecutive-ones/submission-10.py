class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum, count = 0, 0

        for num in nums:
            if num:
                count += 1 
          
            else:
                count = 0

            maximum = max(count, maximum)
        
        return maximum
