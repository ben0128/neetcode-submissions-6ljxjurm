class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let len = nums.length
        let res = new Array(len).fill(1)
        for (let i=1; i<len; i++){
            res[i] = nums[i-1] * res[i-1]
        }
        console.log(res)
        let temp = 1
        for (let i=len-1; i>=0; i--) {
            res[i] = res[i] * temp
            temp = nums[i] * temp
        }
        return res
    }
}
