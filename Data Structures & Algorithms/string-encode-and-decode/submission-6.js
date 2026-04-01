class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let res = '';
        for (const str of strs) {
            res += `${str.length}#${str}`
        }
        return res;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let res = [];
        let num = '';
        for (let i=0; i<str.length; i++) {
            if (str[i] !== '#') {
                num += str[i];
                continue;
            }
            res.push(str.slice(i+1, Number(num)+i+1))
            i += Number(num)
            num = ''
        }
        return res
    }
}