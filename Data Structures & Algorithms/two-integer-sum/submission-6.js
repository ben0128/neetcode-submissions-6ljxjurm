class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = new Map()
        for (let idx=0; idx<nums.length;idx++){
            let diff = target - nums[idx]
            let checkExist = map.has(diff)
            if (checkExist) return [map.get(diff), idx]
            map.set(nums[idx], idx)
        }
        return [-1, -1]
    }
}
