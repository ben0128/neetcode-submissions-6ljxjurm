class MinStack {
    constructor() {
        this.stack = []
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val)
        return;
    }

    /**
     * @return {void}
     */
    pop() {
        this.stack.pop()
        return;
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack[this.stack.length-1]
    }

    /**
     * @return {number}
     */
    getMin() {
        let min = Infinity;
        this.stack.forEach(item => {
            if (min > item) min = item
        })
        return min
    }
}
