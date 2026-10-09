class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize return string
        ans = ""
        # Loop over index 1 of each string, add to a set.
        charindex = 0

        while True:
            checking = set()
            
            for i in range(len(strs)):
                if len(strs[i]) >= charindex+1:
                    checking.add(strs[i][charindex])
                else:
                    return ans
            
            # If set is length 1, they all match, add that char to return string.  
            if len(checking) == 1:
                ans += "".join(checking)
            
            # If set is more than 1, we don't have a common prefix.  Return ans.
            if len(checking) > 1:
                return ans

            # Repeat on the next char
            charindex += 1

