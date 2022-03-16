
# https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # root 를 기준으로 swap left node ~ right node 
        def _invert(node):
            if not node :
                return 
            node.left,node.right=node.right,node.left
            if node.left : _invert(node.left)
            if node.right : _invert(node.right)
            
        
        if root : 
            _invert(root)
        return root
        
        