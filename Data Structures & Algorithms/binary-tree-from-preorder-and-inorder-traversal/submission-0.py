# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def rec(node, porder, iorder):
            val = porder[0]
            idx = 0
            while iorder[idx] != val:
                idx += 1
            
            if idx >= 1:
                leftPre = porder[1:idx + 1]
                leftIn = iorder[0:idx]
                node.left = TreeNode(porder[1])
                rec(node.left, leftPre, leftIn)
            if idx < len(iorder) - 1 :
                rightPre = porder[idx + 1:]
                rightIn = iorder[idx + 1:]
                node.right = TreeNode(porder[idx + 1])
                rec(node.right, rightPre, rightIn)
            
    
        root = TreeNode(preorder[0])
        rec(root, preorder, inorder)


        return root

            
        