class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        const len = matrix[0].length
        let find = -1;
        for (let i=0; i<matrix.length; i++) {
            if (matrix[i][len-1] >= target) {
                find = i;
                break
            }
        }
        if (find === -1) return false;
        let l = 0, r = len-1;
        while (l<=r) {
            const mid = l + Math.floor((r-l)/2);
            if (matrix[find][mid] === target) return true;
            if (matrix[find][mid]< target) {
                l = mid+1
            } else {
                r = mid-1
            }
        }
        return false
    }
}
