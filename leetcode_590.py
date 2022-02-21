# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(root, result):
            for child in root.children:
                dfs(child, result)
            result.append(root.val)
        
        result = []
        if root:
            dfs(root, result)
        return result
            


        