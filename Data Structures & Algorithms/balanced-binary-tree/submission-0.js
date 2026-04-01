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
        if (!root || (!root.left && !root.right)) return true;
        const dfs = (node) => {
            let left = node.left ? dfs(node.left): [true, 0];
            let right = node.right ? dfs(node.right): [true, 0];
            if (!left[0] || !right[0]) return [false, 0]
            return Math.abs(left[1]-right[1]) > 1 ? [false, 0] : [true, Math.max(left[1], right[1])+1]
        }
        return dfs(root)[0]
    }
}
