class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        let one = 1, two = 2;
        if (n<3) return n;
        for (let i=3; i<n; i++) {
            let temp = one+two;
            one = two, two=temp
        }
        return one+two;
    }
}
