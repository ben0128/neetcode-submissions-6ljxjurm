class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        if (s.length === 1) return true;
        let i = 0, j = s.length-1
        while (i < j){
            let left = s[i].toLowerCase();
            if (!this.isNumAndAlpha(left)) { 
                i++;
                continue;
            }
            let right = s[j].toLowerCase();
            if (!this.isNumAndAlpha(right)) {
                j--;
                continue;
            }
            if (left !== right) return false;
            i++
            j--
        }
        return true;
    }
    
    isNumAndAlpha(str){
        let s = str.charCodeAt()
        if ((s >= 97 && s <= 122) || (s >= 48 && s <= 57)) return true
        return false
    }
}