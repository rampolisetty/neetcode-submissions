class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open_map = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for c in s:
            if c in close_to_open_map:
                if stack and stack[-1] == close_to_open_map[c]:
                    stack.pop() # Pop Open
                else:
                    return False
            else:
                stack.append(c) # Add Open 
        
        return True if not stack else False