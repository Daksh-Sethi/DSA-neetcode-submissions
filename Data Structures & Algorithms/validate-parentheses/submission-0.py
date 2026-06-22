class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack:
                    return False
                elif stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False

        return len(stack)==0
