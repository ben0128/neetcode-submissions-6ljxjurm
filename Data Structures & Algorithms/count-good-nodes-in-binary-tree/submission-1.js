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
     * @return {number}
     */
    goodNodes(root) {
        const dfs = (node, max) => {
            if (!node) return 0;
            const res = node.val >= max ? 1 : 0;
            max = node.val >= max ? node.val : max;
            return res + dfs(node.left, max) + dfs(node.right, max);
        }
        return dfs(root, root.val)
    }
}
