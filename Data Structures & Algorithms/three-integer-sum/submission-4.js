class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        nums.sort((a,b)=>a-b)
        const ans = [];
        let len = nums.length
        if (nums[0]>0 || nums[len-1]<0) return ans
        for (let i=0; i<len-2; i++) {
            if (i>0 && nums[i] === nums[i-1]) continue
            let j = i+1, k = len-1;
            if (nums[i]+nums[j]+nums[j+1]>0) break;
            if (nums[i]+nums[k-1]+nums[k]<0) continue;
            while (j<k) {
                const sum = nums[i]+nums[j]+nums[k]
                while(nums[j+1] === nums[j]) j++;
                while(nums[k-1] === nums[k]) k--;
                if (sum === 0) {
                    ans.push([nums[i],nums[j],nums[k]])
                    j++;
                    k--;
                } else if (sum > 0) {
                    k--
                } else {
                    j++
                }
            }
        }
        return ans
    }
}
