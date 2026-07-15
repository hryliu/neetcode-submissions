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
    // Helper returns true if subtree is balanced and fills 'height' by reference
    bool dfs(TreeNode* node, int &height) {
        if (!node) {
            height = 0;
            return true;
        }

        int lh = 0, rh = 0;
        // check left and right subtrees; stop early if either unbalanced
        if (!dfs(node->left, lh))  return false;
        if (!dfs(node->right, rh)) return false;

        if (std::abs(lh - rh) > 1)
            return false;               // current node unbalanced

        height = 1 + std::max(lh, rh);  // update height for parent
        return true;
    }

    bool isBalanced(TreeNode* root) {
        int height = 0;
        return dfs(root, height);
    }
};
