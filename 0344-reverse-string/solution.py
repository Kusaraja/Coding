class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s[:] = s[::-1]
        start = 0
        for end in range(len(s)-1,-1,-1):
            if start < end:
                s[start] , s[end] = s[end] , s[start]
                start += 1
                end -= 1