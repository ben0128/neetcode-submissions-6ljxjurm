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
     * @return {TreeNode}
     */
    invertTree(root) {
        if (!root) return root;
        const change = (node) => {
            if (!node) return ;
            [node.right, node.left] = [node.left, node.right]
            change(node.right);
            change(node.left);
        }
        change(root);
        return root;
    }
}
