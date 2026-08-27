class Solution:
    def isValid(self, s: str) -> bool:
        def isLeft(c):
            return c == '(' or c == '{' or c == '['
        def matches(c1, c2):
            if c1 == '(':
                return c2 == ')'
            elif c1 == '{':
                return c2 == '}'
            elif c1 == '[':
                return c2 == ']'
            return False
            
        stack = []
        
        for i in range(len(s)):
            c1 = s[i]
            if isLeft(c1):
                stack.append(c1)
            else:
                if len(stack) == 0:
                    return False
                c2 = stack.pop()
                if not matches(c2, c1):
                    return False
        return len(stack) == 0
