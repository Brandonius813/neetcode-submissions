class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            
            if pair in vals:
                return [vals[pair], i]

            vals[nums[i]] = i
