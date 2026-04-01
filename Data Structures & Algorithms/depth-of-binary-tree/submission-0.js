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
    maxDepth(root) {
        if (!root) return 0;
        let max = -Infinity;
        const findDeep = (node, temp) => {
            if (!node) return;
            temp++;
            max = Math.max(max, temp)
            findDeep(node.left, temp);
            findDeep(node.right, temp);
        }
        findDeep(root, 0);
        return max;
    }
}
