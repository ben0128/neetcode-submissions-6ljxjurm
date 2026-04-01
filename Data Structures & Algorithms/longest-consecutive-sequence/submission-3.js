class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        if (nums.length === 0) return 0
        let set = new Set(nums);
        let maxLen = 1;
        let tempLen = 1;
        for (let num of nums) {
            if (!set.has(num)) continue
            set.delete(num)
            let tempNum = num;
            while (set.has(tempNum-1)) {
                tempLen++;
                tempNum--;
                set.delete(tempNum);
            }
            tempNum = num;
            while (set.has(tempNum+1)) {
                tempLen++;
                tempNum++;
                set.delete(tempNum);
            }
            maxLen = tempLen > maxLen ? tempLen : maxLen;
            tempLen = 1
        }
        return maxLen;
    }
}
