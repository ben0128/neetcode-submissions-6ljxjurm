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
        if (!root) return false;
        let findRes = [];
        const findNode = (node) => {
            if (!node) return null;
            if (node.val === subRoot.val) findRes.push(node);
            const resL = findNode(node.left);
            if (resL) return resL;
            const resR = findNode(node.right);
            if (resR) return resR;
            return null;
        }
        findNode(root);
        if (findNode.length === 0) return false;
        for ( let item of findRes) {
            if (this.dfs(item, subRoot)) return true
        }
        return false
    }
    
    dfs(n1, n2) {
        if (!n1 && !n2) return true;
        if (!n1 || !n2 || n1.val !== n2.val) return false;

        const resL = this.dfs(n1.left, n2.left);
        const resR = this.dfs(n1.right, n2.right);

        if (!resL || !resR) return false;
        return true;
    }
    
}
