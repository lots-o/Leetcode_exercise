# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        values=[]
        def _inorder(root,values):
            if root is None:
                return  
            _inorder(root.left,values)
            values.append(root.val)
            _inorder(root.right,values)
            
        _inorder(root,values)
        
        ans=cursor=TreeNode(None)
        for val in values:
            cursor.right=TreeNode(val)
            cursor=cursor.right
        
        return ans.right
                
            
        

        