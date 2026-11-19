class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        
        for i, num in enumerate(nums):
            pair = target - num
            if pair in checked:
                return [checked[pair], i]
        
            else:
                checked[num] = i
