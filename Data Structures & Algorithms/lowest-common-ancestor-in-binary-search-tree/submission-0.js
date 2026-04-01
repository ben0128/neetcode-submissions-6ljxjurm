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
        const need = [p.val, q.val];
        let roads = [[], []];
        const dfs = (node, road) => { 
            if (!node){
                return false;
            }
            road.push(node);
            if (need.indexOf(node.val) !== -1) {
                roads[need.indexOf(node.val)] = road;
                if (roads[0].length > 0 && roads[1].length > 0) return true;
            }
            const resL = dfs(node.left, [...road]);
            if (resL) return true;
            const resR = dfs(node.right, [...road]);
            if (resR) return true;
            road.pop();
            return false;
        }
        dfs(root, [])
        if (roads[0].length <= roads[1].length) [roads[0], roads[1]] = [roads[1], roads[0]];
        for (let i=0; i<roads[0].length; i++){
            if (!roads[1][i] || roads[0][i].val !== roads[1][i].val) return roads[0][i-1];
        }
    }
}

// 0, 1, 2, 3
// 0, 1, 5
