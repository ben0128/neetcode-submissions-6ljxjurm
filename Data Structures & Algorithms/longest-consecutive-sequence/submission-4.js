class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        if (nums.length === 0) return 0
        let set = new Set(nums);
        let maxLen = 1;
        for (let num of nums) {
            if (set.has(num-1)) continue
            let tempNum = num;
            while (set.has(tempNum+1)) {
                tempNum++
            }
            maxLen = (tempNum-num+1) > maxLen ? (tempNum-num+1) : maxLen;
        }
        return maxLen;
    }
}
