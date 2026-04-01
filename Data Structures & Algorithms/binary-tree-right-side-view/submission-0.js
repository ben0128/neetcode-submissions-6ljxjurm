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
     * @return {number[]}
     */
    rightSideView(root) {
        if (!root) return [];
        const temp = [root];
        const ans = [];
        while (temp.length > 0) {
            for (let i=0, len=temp.length; i<len; i++) {
                let node = temp.shift();
                if (i === len-1) ans.push(node.val);
                if (node.left) temp.push(node.left);
                if (node.right) temp.push(node.right);
            }
        }
        return ans
    }
}
