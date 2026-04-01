class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;
        let arr = new Array(26).fill(0);
        for (let str of s){
            arr[str.charCodeAt()-97]++;
        }
        for (let str of t){
            arr[str.charCodeAt()-97]--;
        }
        for (let num of arr){
            if (num !== 0) return false
        }
        return true
    }
}
