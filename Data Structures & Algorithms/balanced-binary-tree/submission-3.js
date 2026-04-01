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
    isBalanced(root) {
        if (!root) return true;
        const dfs = (node) => {
            let left = node.left ? dfs(node.left): 0;
            let right = node.right ? dfs(node.right): 0;
            if (left === -1 || right === -1 || Math.abs(left-right) > 1) return -1;
            return  Math.max(left, right)+1;
        }
        return dfs(root) !== -1
    }
}
