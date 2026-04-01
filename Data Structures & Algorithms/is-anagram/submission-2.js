class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;
        const arr = new Array(26).fill(0);
        for (let i=0; i<s.length;i++){
            arr[s[i].charCodeAt()-'a'.charCodeAt()]++;
            arr[t[i].charCodeAt()-'a'.charCodeAt()]--
        }
        for (let num of arr){
            if (num !== 0) return false
        }
        return true
    }
}
