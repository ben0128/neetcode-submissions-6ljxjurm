class Solution {
    /**
     * @param {number[]} temp
     * @return {number[]}
     */
    dailyTemperatures(temp) {
        if (temp.length === 1) return [0]
        const ans = [0]
        const len = temp.length
        let max = temp[len-1];
        
        for (let i=len-2; i>=0; i--) {
            if (temp[i] < max) {
                let findIdx = i;
                while (findIdx<=len-1){
                    if (temp[findIdx] > temp[i]) {
                        ans.push(findIdx-i);
                        break
                    }
                    findIdx++;
                }
            } else {
                max = temp[i];
                ans.push(0)
            }
        }
        return ans.map((_, idx) => ans[len-idx-1])
    }
}
