class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        let left = 0, right = nums.length-1;
        let mid = left + Math.floor((right-left)/2)
        while (left <= right) {
            if (nums[left] > nums[mid] && nums[right] > nums[mid]) {
                right = mid;
            } else if (nums[left] < nums[mid] && nums[right] < nums[mid]) {
                left = mid;
            }
            mid = left + Math.floor((right-left)/2);
            if (nums[left] >= nums[mid] && nums[mid] >= nums[right]) {
                return nums[right]
            } else if (nums[left] <= nums[mid] && nums[mid] <= nums[right]){
                return nums[left]
            }
        }
    }
}
