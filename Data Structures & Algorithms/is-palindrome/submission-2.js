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
            let left = s[i].toLowerCase();
            if (!/^[a-z0-9]$/.test(left)) { 
                i++;
                continue;
            }
            let right = s[j].toLowerCase();
            if (!/^[a-z0-9]$/.test(right)) {
                j--;
                continue;
            }
            if (left !== right) return false;
            i++
            j--
        }
        return true;
    }
}