class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let hash = {}, start = 0, max = 0
        for (let i=0, len=s.length; i<len; i++) {
            if (hash[s[i]] !== undefined && hash[s[i]] >= start) {
                start = hash[s[i]] + 1;
            }
            max = Math.max(max, i-start+1)
            if (len-start < max) return max
            hash[s[i]] = i;
        }
        return max
    }
}

// 0 1 2 3