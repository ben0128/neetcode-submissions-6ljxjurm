class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        if (s.length === 1) return true;
        let arr = s.split('')
        console.log(arr)
        let i = 0, j = s.length-1
        while (i < j){
            let left = s[i].toLowerCase().charCodeAt();
            if ((0 > left-'a'.charCodeAt()) || (left-'a'.charCodeAt()) > 25) {
                if (isNaN(parseInt(s[i]))) {
                    i++;
                    continue;
                }
            }
            let right = s[j].toLowerCase().charCodeAt();
            if ((0 > right-'a'.charCodeAt()) || (right-'a'.charCodeAt()) > 25) {
                if (isNaN(parseInt(s[j]))) {
                    j--;
                    continue;
                }
            }
            if (left !== right) return false;
            i++
            j--
        }
        return true;
    }
}