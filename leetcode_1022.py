
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def _search(node,candidate,bin_result):
            if not node.left and not node.right :  # leaf node 
                bin_result.append(candidate[:]+[node.val])
                if candidate : candidate.pop() # backtracking
                return  
            else : 
                candidate.append(node.val)
                if node.left : _search(node.left,candidate[:],bin_result)
                if node.right : _search(node.right,candidate[:],bin_result)
                

        bin_result=[]
        candidate=[]
        _search(root,candidate,bin_result)
        
        # bin2decimal 
        decimal_result=[]
        for binary in bin_result:
            decimal_result.append(int(''.join(map(str,binary)),2))
        
        return sum(decimal_result)
            
        
        
        