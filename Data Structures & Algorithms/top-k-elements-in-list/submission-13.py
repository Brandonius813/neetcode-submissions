# I made 2 mistakes - first, I tried to do list * number.  That didn't work.  Second, I tried to do if counts[i] instead of while counts[i]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Make dict of counts

        countsdict = defaultdict(int)

        for num in nums:
            countsdict[num] += 1

        # Add each value to a list within an array at index counts
        counts = [[] for i in range(len(nums) + 1)]

        for val, cnt in countsdict.items():
            counts[cnt].append(val)


        # Iterate backward through the array.  If I find a list in the array with values in it, start returning them and decrementing K.  Stop when k is 0.
        i = len(nums)
        res = []
        while k > 0:
            while counts[i]:
                add = counts[i].pop()
                res.append(add)
                k -= 1
            
            i -= 1
        
        return res


