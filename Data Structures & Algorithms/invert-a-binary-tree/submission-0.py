# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def rec(root):
            if not root:
                return
            temp = root.left
            root.left = root.right
            root.right = temp
            rec(root.left)
            rec(root.right)
        rec(root)
        return root