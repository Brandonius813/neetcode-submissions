class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        numSet = set(nums)

        maxLen = 1

        for i in range(len(nums)):

            if nums[i] - 1 in numSet:
                continue
            curLen = 1

            while nums[i] + curLen in numSet:
                curLen += 1
            
            maxLen = max(maxLen, curLen)

        return maxLen