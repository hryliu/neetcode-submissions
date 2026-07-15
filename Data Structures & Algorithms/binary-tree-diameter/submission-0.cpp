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
    int maxDiameter = 0;  // global tracker for maximum diameter

    int depth(TreeNode* root) {
        if (!root) return 0;

        // compute left and right subtree heights
        int left = depth(root->left);
        int right = depth(root->right);

        // update diameter if path through this node is longer
        maxDiameter = max(maxDiameter, left + right);

        // return height of this subtree
        return 1 + max(left, right);
    }

    int diameterOfBinaryTree(TreeNode* root) {
        depth(root);               // helper to compute diameters
        return maxDiameter;        // result = max path length
    }
};
