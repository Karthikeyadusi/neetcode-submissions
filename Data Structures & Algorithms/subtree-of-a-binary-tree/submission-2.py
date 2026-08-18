# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p,q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            else:
                return p.val == q.val and sameTree(p.left, q.left) and sameTree(p.right, q.right)
        def subTree(p,q):
            if p is None:
                return False
            return sameTree(p,q) or subTree(p.left, q) or subTree(p.right,q)
        return subTree(root, subRoot)                
        