# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def _search(node,count,depth_lst):
            if not node.left and not node.right :
                depth_lst.append(count+1)
            else:
                count+=1
                if node.left : _search(node.left,count,depth_lst)
                if node.right : _search(node.right,count,depth_lst)
                
            
        count=0
        depth_lst=[]
        if root :
            _search(root,count,depth_lst)
            return max(depth_lst)
        else :
            return 0

                
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
                       
        return dfs(root, 0)
            
            
            
            
            
        
        