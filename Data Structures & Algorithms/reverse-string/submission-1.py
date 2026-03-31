class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        if length == 0:
            return
        
        start = 0
        end = length - 1
        while start < end:
           s[start], s[end] = s[end], s[start]
           start += 1
           end -= 1
        

        