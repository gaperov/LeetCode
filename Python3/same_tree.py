# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(root_p, root_q):
            if not root_p and not root_q:
                return True
            elif not root_p or not root_q:
                return False
            else:
                if root_p.val == root_q.val:
                    if check(root_p.left, root_q.left):
                        if check(root_p.right, root_q.right):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        
        ans = check(p, q)
        return ans
                
