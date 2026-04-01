class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let l = 0, r = nums.length-1; // 0, 5
        while (l<=r) {
            const mid = l + Math.floor((r-l)/2);
            if (nums[mid] < target) {
                l = mid+1;
            } else if (nums[mid] > target){
                r = mid-1;
            } else {
                return mid
            }
        }
        return -1
    }
}
