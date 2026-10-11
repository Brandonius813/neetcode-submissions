class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        maxnum, occ, cnt = nums[0], 0, 0
        firstnum = nums[0]
        for num in nums:
            if num == firstnum:
                occ += 1
            if num != firstnum:
                if occ > cnt:
                    cnt = occ
                    maxnum = firstnum
                occ = 1
                firstnum = num
        if occ > cnt:
            maxnum = firstnum
        
        return maxnum
