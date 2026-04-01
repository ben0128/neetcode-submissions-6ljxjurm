/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    isValidBST(root) {
        if (!root) return true;
        const dfs = (node, left, right) => {
            if (!node) return true;
            if (node.val > left && node.val < right){
                return dfs(node.left, left, node.val) && dfs(node.right, node.val, right);
            }
            return false;
        }
        return dfs(root, -Infinity, Infinity);
    }
}
