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
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {TreeNode}
     */
    lowestCommonAncestor(root, p, q) {
        // dfs 左到右,沿路紀錄路徑直到找到第一個點
        if (p.val > q.val) [p, q] = [q, p];
        while (true) {
            if (root.val >= p.val && root.val <= q.val) {
                break;
            } else if (root.val < p.val && root.val < q.val){
                root = root.right
            } else {
                root = root.left
            }
        }
        return root
    }
}

// 0, 1, 2, 3
// 0, 1, 5
