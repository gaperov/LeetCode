class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in {'(', '{', '['}:
                stack.append(c)
            else:
                if stack:
                    top = stack.pop()
                    if c == ')' and top != '(':
                        return False
                    if c == ']' and top != '[':
                        return False
                    if c == '}' and top != '{':
                        return False
                else:
                    return False
        return len(stack) == 0
