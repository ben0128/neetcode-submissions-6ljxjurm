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
     * @return {number[][]}
     */
    levelOrder(root) {
        const dfs = (node, level, nodeMap) => {
            if (!node) return [];
            
            if (!nodeMap[level]) nodeMap[level] = [node.val];
            else nodeMap[level].push(node.val);

            dfs(node.left, level+1,nodeMap);
            dfs(node.right, level+1, nodeMap);
            return nodeMap
        }
        return dfs(root, 0, [])
    }
}
