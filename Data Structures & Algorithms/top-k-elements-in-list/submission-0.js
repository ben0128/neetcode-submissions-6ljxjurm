class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const cal = {}
        for (let item of nums) {
            cal[item] = (cal[item] || 0 ) + 1;
        }
        console.log(cal)
        const bucket = Array(nums.length+1).fill().map(()=>[])
        for (let i in cal){
            console.log(i)
            bucket[cal[i]].push(i)
        }
        let ans = []
        for (let i=bucket.length-1; i>=0;i--){
            bucket[i].forEach(j=> ans.push(j))
            if (ans.length === k) return ans
        }
        return ans
    }
}
