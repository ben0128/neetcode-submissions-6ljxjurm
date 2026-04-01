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
        let ans = 0;
        const dfs = (node, max) => {
            if (max <= node.val) {
                ans++;
                max = node.val;
            }
            if (node.left) dfs(node.left, max)
            if (node.right) dfs(node.right, max)
            return ans;
        }
        return dfs(root, root.val)
    }
}
