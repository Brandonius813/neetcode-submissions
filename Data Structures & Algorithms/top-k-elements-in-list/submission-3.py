class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    # Options include: Sorting the array, then taking the most frequent values (nLogn time best case?),     
    
    # This is a bucket sort problem... finite number of buckets, sort array into those buckets, take the largest ones, return their values.
    # Make a hashmap that counts occurrances of each value, that is "pre-sorted" in highest to lowest order.

    # A difference from my first attempt is the keys are counts, then value is a lsit of integers who occur that number of times.

    #OHH you can make a hashmap of counts/value, then MAP THAT to the next hashmap of count/[values].  It's just 3n space complexity.  I psyched myself out.

        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        freq = [[] for i in range(len(nums) + 1)]
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res