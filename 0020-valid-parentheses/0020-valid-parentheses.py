class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                # If stack is empty or brackets don't match, it's invalid
                if not stack:
                    return False
                top = stack.pop()
                if char == ')' and top != '(':
                    return False
                if char == '}' and top != '{':
                    return False
                if char == ']' and top != '[':
                    return False
                    
        return not stack