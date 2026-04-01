class Solution {
    /**
     * @param {number[]} temp
     * @return {number[]}
     */
    dailyTemperatures(temp) {
        const len = temp.length;
        const ans = new Array(len).fill(0);
        let max = temp[len-1];
        
        for (let i=len-2; i>=0; i--) {
            if (temp[i] < max) {
                let findIdx = i;
                while (findIdx<=len-1){
                    if (temp[findIdx] > temp[i]) {
                        ans[i] = findIdx-i;
                        break
                    }
                    findIdx++;
                }
            } else {
                max = temp[i];
            }
        }
        return ans
    }
}
