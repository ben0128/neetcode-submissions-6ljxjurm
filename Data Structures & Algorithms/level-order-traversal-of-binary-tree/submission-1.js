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
        if (!root) return []
        const tempArr = [root];
        const ans = [];
        while (tempArr.length > 0) {
            ans[ans.length] = [];
            for (let i=0, len=tempArr.length; i<len; i++) {
                let node = tempArr.shift();
                ans[ans.length-1].push(node.val);
                if (node.left) tempArr.push(node.left);
                if (node.right) tempArr.push(node.right);
            }
        }
        return ans;
    }
}
