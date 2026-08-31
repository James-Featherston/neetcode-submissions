class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxi = 0

        for h in heights:
            if not stack:
                stack.append((h, 1))
            elif h > stack[-1][0]:
                stack.append((h, 1))
            else: # if there is one that is greater than or equal to, we need to calculate the area, pop it, take the length, add it to the current one and add that one
                prev_len = 0
                while stack and stack[-1][0] >= h:
                    cur_h, cur_l = stack.pop()
                    maxi = max(maxi, cur_h * (cur_l + prev_len))
                    prev_len += cur_l
                stack.append((h, prev_len + 1))
        
        while stack:
            h, length = stack.pop()
            maxi = max(maxi, h * length)
            if stack:
                old_h, old_length = stack.pop()
                stack.append((old_h, old_length + length))


        return maxi

        