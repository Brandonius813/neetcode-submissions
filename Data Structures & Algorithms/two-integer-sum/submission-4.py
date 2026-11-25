class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        out = []

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in checked:
                out = [checked[pair], i]
                return out
            
            checked[nums[i]] = i