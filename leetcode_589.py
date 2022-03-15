# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(root, result):
            result.append(root.val)
            for child in root.children:
                dfs(child,result)
        
        result = []
        if root:
            dfs(root, result)
        return result
    
    
    