class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;
        let hash = {}
        for (let str of s){
            hash[str] = hash[str] ? hash[str]+1 : 1;
        }
        for (let str of t){
            if (hash[str]){
                if (hash[str]>1){
                    hash[str] = hash[str]-1;
                } else {
                    delete hash[str]
                }
            } else {
                return false
            }
        }
        return JSON.stringify(hash) === '{}';
    }
}
