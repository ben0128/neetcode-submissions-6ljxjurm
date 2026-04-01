class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        if (s.length%2 !== 0) return false
        const hash = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        const stack = [];
        for (let i of s) {
            if (!hash[i]) {
                stack.push(i);
            } else {
                let last = stack.pop();
                if (last !== hash[i]) return false;
            }
        }
        return stack.length === 0;
    }
}
