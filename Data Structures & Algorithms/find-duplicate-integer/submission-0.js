class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findDuplicate(nums) {
        let hash = {}
        for (let item of nums){
            if (hash[item]) return item
            hash[item] = true;
        }
    }
}
