class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = []
        for i in s:
            if i in ('(', '{', '['):
                stack1.append(i)
            elif i == ')':
                if not stack1:
                    return False
                if stack1.pop() != "(":
                    return False
            elif i == '}':
                if not stack1:
                    return False
                if stack1.pop() != "{":
                    return False
            elif i == ']':
                if not stack1:
                    return False
                if stack1.pop() != "[":
                    return False         
        return not stack1