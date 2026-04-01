class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        if (s1.length > s2.length) return false;
        let count = new Array(26).fill(0);
        const base = 'a'.charCodeAt();
        for (let idx=0; idx<s1.length; idx++){
            const str = s1[idx]
            count[str.charCodeAt()-base]++;
            count[s2[idx].charCodeAt()-base]--;
        }
        if (count.every(x => x === 0)) return true;
        for (let j=s1.length; j<s2.length; j++){
            count[s2[j].charCodeAt()-base]--;
            count[s2[j-s1.length].charCodeAt()-base]++;
            if (count.every(x => x === 0)) return true;
        }
        return false;
    }
}
