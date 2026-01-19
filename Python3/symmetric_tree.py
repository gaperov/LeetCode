# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(root_l, root_r):
            if not root_l and not root_r:
                return True
            elif not root_l or not root_r:
                return False
            else:
                if root_l.val == root_r.val:
                    if check(root_l.left, root_r.right):
                        if check(root_l.right, root_r.left):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        
        ans = check(root.left, root.right)
        return ans
        
