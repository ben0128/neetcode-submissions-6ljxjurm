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
     * @param {TreeNode} subRoot
     * @return {boolean}
     */
    isSubtree(root, subRoot) {
        if (!subRoot) return true;
        const findNode = (node) => {
            if (!node) return false;
            if (node.val === subRoot.val) {
                if (this.dfs(node, subRoot)) return true;
            }
            return findNode(node.left) || findNode(node.right);
        }
        return findNode(root);
    }
    
    dfs(n1, n2) {
        if (!n1 && !n2) return true;
        if (!n1 || !n2 || n1.val !== n2.val) return false;
        return this.dfs(n1.left, n2.left) && this.dfs(n1.right, n2.right);
    }
}
