class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        maxa = 0
        while l < r:
            lh, rh = heights[l], heights[r]
            height = min(lh, rh)
            area = (r - l) * height

            maxa = max(maxa, area)

            if lh < rh:
                l += 1
            elif lh > rh:
                r -= 1
            else:
                if heights[l + 1] < heights[r - 1]:
                    r -= 1
                else:
                    l += 1
        return maxa
            