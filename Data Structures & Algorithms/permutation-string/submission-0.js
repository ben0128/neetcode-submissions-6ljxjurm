class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        let origin = {}
        for (let str of s1) {
            if (!origin[str]) origin[str] = 0;
            origin[str]++;
        }
        let copy = JSON.parse(JSON.stringify(origin))
        for (let i=0,len=s2.length; i<len;i++){
            if (origin[s2[i]] === undefined) continue;

            for (let j=0; j<s1.length; j++){
                if (copy[s2[j+i]] && copy[s2[j+i]]>0) {
                    copy[s2[j+i]]--;
                    if (j === s1.length-1) return true;
                } else if (copy[s2[j+i]] && copy[s2[j+i]] === 0) {
                    copy = JSON.parse(JSON.stringify(origin))
                    break;
                } else {
                    copy = JSON.parse(JSON.stringify(origin))
                    break;
                }
            }
        }
        return false
    }
}
