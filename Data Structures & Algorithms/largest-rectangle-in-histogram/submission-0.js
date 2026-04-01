class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    largestRectangleArea(heights) {
        heights = [0, ...heights, 0]
        const stack = [], len = heights.length;
        let max = 0;
        for (let i = 0; i<len; i++) {
            while (stack.length > 0 && heights[i] < heights[stack[stack.length-1]]) {
                const height = heights[stack.pop()];
                const width = i - stack[stack.length-1] - 1;
                max = Math.max(height*width, max)
            }
            stack.push(i)
        }
        return max
    }
}