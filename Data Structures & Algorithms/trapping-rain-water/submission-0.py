class Solution:
    def trap(self, height: List[int]) -> int:
        LEN = len(height)
        larr = [0] * LEN
        rarr = [0] * LEN

        lmax = 0
        rmax = 0
        for i in range(0, LEN):
            lmax = max(height[i], lmax)
            larr[i] = lmax

            rmax = max(height[LEN - i - 1], rmax)
            rarr[LEN - i - 1] = rmax
        
        count = 0
        for i in range(0, LEN):
            minh = min(rarr[i], larr[i])
            if minh > height[i]:
                count += minh - height[i]
        
        return count