class Solution {
    /**
     * @param {number[]} temp
     * @return {number[]}
     */
    dailyTemperatures(temp) {
        const ans = new Array(temp.length-1).fill(0);
        const stack = [[temp[0], 0]];
        for (let i=1, len=temp.length; i<len; i++){
            while (stack.length > 0 && stack[stack.length-1][0] < temp[i] ) {
                let last = stack.pop()
                ans[last[1]] = i-last[1];
            }
            stack.push([temp[i], i])
            console.log(ans)
        }
        ans.push(0)
        return ans
    }
}
