class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let left = [1]
        let right = [1]
        let len = nums.length -1
        for (let i=1;i<=len; i++) {
            left.push(left[i-1]*nums[i-1])
            right.push(right[i-1]*nums[len-i+1])
        }
        return left.map((item,idx) => {
            return left[idx] * right[len - idx]
        })
    }
}
