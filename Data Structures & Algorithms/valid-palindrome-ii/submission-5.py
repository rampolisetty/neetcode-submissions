class Solution:
    # Time O(n), Space O(1)
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r) -> bool:
            while l < r:
                if not s[l].isalnum():
                    l += 1
                    continue
                if not s[r].isalnum():
                    r -= 1
                    continue
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l].lower() != s[r].lower():
                return isPalindrome(l + 1, r) or isPalindrome(l, r - 1)
            l += 1
            r -= 1
        return True
