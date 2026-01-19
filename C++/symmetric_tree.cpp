/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        bool ans = check(root->left, root->right);
        return ans;
    }
private:
    bool check(TreeNode* root_r, TreeNode* root_l){
        if (!root_r && !root_l) {
            return true;
        } else if (!root_l || !root_r) {
            return false;
        } else {
            if (root_r->val == root_l->val) {
                if (check(root_l->left, root_r->right)){
                    if (check(root_l->right, root_r->left)) {
                        return true;
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }
    }
};
