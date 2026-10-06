class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcons, cur = 0, 0

        for num in nums:
            if num:
                cur += 1
            
            maxcons = max(maxcons, cur)

            if not num:
                cur = 0
            
        return maxcons
