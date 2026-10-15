class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Make a hashmap of val:count (O(n) time)

        # Make an array of occurrances:[val, val] - example: 3x: [12, 4, 7] each happened 3 times (O(n) time)

        # Iterate thru the array backwards, whenever I get to values, add those to my return array and decrement k.  Once k hits zero, return the array.  (Worst case, O(n) time)

        # This is Big O 3n, so just O(n).  Same for space complexity - 1 hashmap, 1 array, so 2-3n worst-case but still linear.
    
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        countlist =[[] for n in (range(len(nums) + 1))]

        for value, count in counts.items():
            countlist[count].append(value)
        
        r = len(countlist) - 1
        out = []


        for i in range(len(nums), -1, -1):
            while len(countlist[i]) > 0 and k > 0:
                tmp = countlist[i].pop()
                out.append(tmp)
                k -= 1
        
        return out




