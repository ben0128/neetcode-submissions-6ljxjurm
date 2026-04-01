class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let hist = {}
        for (let str of strs) {
            let arr = Array(26).fill(0)
            for (let i of str) {
                arr[i.charCodeAt()-'a'.charCodeAt()]++
            }
            let sum = arr.join("#")
            if (!hist[sum]) {
                hist[sum] = [str]
            } else {
                hist[sum].push(str)
            }   
        }
        return Object.values(hist)
    }
}
