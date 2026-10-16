class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        cur, swap = 0, -1

        for char in range(len(s) // 2):
            tmp = s[cur]
            s[cur] = s[swap]
            s[swap] = tmp

            cur += 1
            swap -= 1

