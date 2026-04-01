class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n) {
        let ans = []
        function loop(l, r, str, idx) {
            if (l+1 <= n && l+1 >= r) {
                loop(l+1, r, str+'(', idx+1)
            }
            if (r+1 <= n && l >= r+1) {
                loop(l, r+1, str+')', idx+1)
            }
            if (idx === n*2) ans.push(str)
            return;
        }
        loop(1, 0, '(', 1)
        return ans
    }
}
