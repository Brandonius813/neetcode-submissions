class TimeMap:

    def __init__(self): #Create the store of values
        self.store = {} # key = string, value = [list of [value, time]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Add this key to the dict if it's not there yet
        if key not in self.store:
            self.store[key] = []
        
        # Dump the pair into the correct value with the value + timestamp
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, []) # This is the array stored at key


        # Binary search through the list of values at key to find the value that's closest to this timestamp.
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l+r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0] #This is the closest we've seen so far, if our binary search finishes without an exct match, still return this
                l = m + 1
            
            else:
                r = m - 1 #We're "over the timestamp" now - that is invalid.  Won't happen.  So no need to update our result value.

            # We're not writing a speed optimal binary search because we don't have an explicit if m == call, but the time complexity is still log(n) and this is a good bit simpler code.
        
        return res

        
