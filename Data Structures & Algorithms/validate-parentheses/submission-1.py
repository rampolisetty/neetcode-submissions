class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open_map = {"}" : "{", ")" : "(", "]" : "["}

        for c in s:
            # Match key
            if c in close_to_open_map:
                if stack and stack[-1] == close_to_open_map[c]:
                    stack.pop() # Pop open
                else:
                    return False # Mismatch
            else:
                # Add open
                stack.append(c)
        
        return True if not stack else False