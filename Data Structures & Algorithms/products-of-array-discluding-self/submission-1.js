class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let len = nums.length -1
        let left = new Array(len+1).fill(1)
        let right = new Array(len+1).fill(1)
        for (let i=1;i<=len; i++) {
            left[i] = left[i-1]*nums[i-1]
            right[i] = right[i-1]*nums[len-i+1]
        }
        return left.map((item,idx) => {
            return left[idx] * right[len - idx]
        })
    }
}
