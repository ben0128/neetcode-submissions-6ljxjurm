class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        const hash = {
            "+": (a, b) => a + b,
            "-": (a, b) => a - b, 
            "*": (a, b) => a * b,
            "/": (a, b) => {
                return Math.trunc(a / b);;
            }
        }
        const stack = [Number(tokens[0])];

        for (let i = 1, len = tokens.length ; i<len; i++) {
            if (!hash[tokens[i]]) {
                stack.push(Number(tokens[i]))
            } else {
                const num1 = stack.pop(), num2 = stack.pop()
                let res = hash[tokens[i]](num2, num1)
                console.log('res', res , num1, num2)
                stack.push(res)
            }
        }
        return stack.pop()
    }
}
