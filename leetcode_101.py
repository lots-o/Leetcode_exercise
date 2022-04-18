# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def _check(left,right):
            if left is None and right is None :
                return True 
            elif left is None or right is None :
                return False 
            elif left.val !=right.val:
                return False
            else :
                return _check(left.left,right.right) and \
                       _check(left.right,right.left)
            
        
        if not root : 
            return True 
        else:
            return _check(root.left,root.right)
    
    
    
    
            