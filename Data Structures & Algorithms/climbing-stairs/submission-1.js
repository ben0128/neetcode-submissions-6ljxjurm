class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        const hist = {};
        const dfs = (level) => {
            if (level === 1 || level === 2) return level;
            hist[level-2] = (hist[level-2] ?? dfs(level-2));
            hist[level-1] = (hist[level-1] ?? dfs(level-1));
            return hist[level-2] + hist[level-1];
        }
        return dfs(n);
    }
}
