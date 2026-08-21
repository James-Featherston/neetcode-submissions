class Solution:
    def isValid(self, s: str) -> bool:

        openParen = ['{', '(', '[']
        closeParen = ['}', ')', ']']
        stack = []

        for paren in s:
            if paren in openParen:
                stack.append(paren)
            else:
                if not len(stack):
                    return False
                left = stack.pop()
                idx = closeParen.index(paren)
                if left != openParen[idx]:
                    return False
        
        if len(stack) > 0:
            return False
        return True
            
        