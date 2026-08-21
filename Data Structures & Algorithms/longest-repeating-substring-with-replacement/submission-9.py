class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alpha = [0] * 26
        longest = 0

        l, r = 0, 0

        while r < len(s):
            alpha[idx(s[r])] += 1
            if r - l + 1 > max(alpha) + k:
                alpha[idx(s[l])] -= 1
                l += 1
                alpha[idx(s[r])] -= 1
            else:
                longest = max(longest, r - l + 1)
                r += 1
            print(longest)
        return longest


def idx(char):
    return ord(char) - ord('A')

                
            
        