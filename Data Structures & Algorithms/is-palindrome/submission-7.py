class Solution:
    def isPalindrome(self, s: str) -> bool:

        def checkValid(c):
            if ord(c) >= ord("a") and ord(c) <= ord("z"):
                return True
            if ord(c) >= ord("0") and ord(c) <= ord("9"):
                return True
            return False
        if not s:
            return True
        s = s.lower()
        l = 0
        r = len(s) - 1

        while l < r:
            if not checkValid(s[l]):
                l += 1
                continue
            if not checkValid(s[r]):
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        
            
            
        