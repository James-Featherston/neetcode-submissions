class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphanumeric(s):
            if (ord(s) <= ord("z") and ord(s) >= ord("a")) or (ord(s) <= ord("9") and ord(s) >= ord("0")):
                return True
            return False
        
        l, r = 0, len(s) - 1

        s = s.lower()
        while l < r:
            if not alphanumeric(s[l]):
                l += 1
            elif not alphanumeric(s[r]):
                r -= 1
            elif s[l] != s[r]:
                return False
            else:
                r -= 1
                l += 1
        return True


        
            
            
        