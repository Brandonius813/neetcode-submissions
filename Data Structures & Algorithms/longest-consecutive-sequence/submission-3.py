class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # List to set

        if len(nums) == 0:
            return 0

        numset = set(nums)
        out = 1

        for i in range(len(nums)):
            greater = nums[i] + 1
            less = nums[i] - 1

            if greater in numset:
                if less in numset:
                    continue

                tmp = 1
                while True:
                    if nums[i]+tmp in numset:
                        tmp += 1
                    else:
                        out = max(tmp, out)
                        tmp = 1
                        break
        
        return out