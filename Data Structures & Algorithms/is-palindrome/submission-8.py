class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while (left < right):
            leftChar = s[left].lower()
            rightChar = s[right].lower()
            if not checkCharacter(leftChar):
                left += 1
            elif not checkCharacter(rightChar):
                right -= 1
            else:
                if leftChar != rightChar:
                    return False
                else:
                    left += 1
                    right -= 1  
            
        
        return True
def checkCharacter(char):
    lowerChar = char.lower()
    if (ord(lowerChar) <= ord('z') and ord(lowerChar) >= ord('a')) or (ord(lowerChar) <= ord('9') and ord(lowerChar) >= ord('0')):
        return True
    return False
        
            
            
        