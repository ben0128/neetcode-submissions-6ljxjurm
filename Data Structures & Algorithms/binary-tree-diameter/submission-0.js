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
    diameterOfBinaryTree(root) {
        const res = [0];
        this.dfs(root, res)
        return res[0];
    }
    dfs(node, res){
        if (!node) return 0;
        let left = this.dfs(node.left, res);
        let right = this.dfs(node.right, res);
        res[0] = Math.max(res[0], left+right); // 更新當下最長
        return Math.max(left, right) + 1 // 更新當前分支左或右最長長度
    }
}
