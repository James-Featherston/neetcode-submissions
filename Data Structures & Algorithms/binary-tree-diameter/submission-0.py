# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam, _ = self.recurseDepth(root)
        return max_diam

    def recurseDepth(self, root: Optional[TreeNode]):
        if not root:
            return (0, 0) # (max_dia, depth)

        leftDepth = self.recurseDepth(root.left)
        rightDepth = self.recurseDepth(root.right) 

        max_diam = max(leftDepth[0], rightDepth[0], leftDepth[1] + rightDepth[1])
        new_depth = max(leftDepth[1], rightDepth[1]) + 1
        return (max_diam, new_depth)