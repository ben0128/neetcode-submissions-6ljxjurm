class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let max = 0, left = 0, right = heights.length-1;
        while (left<right){
            let temp = (right-left)*Math.min(heights[left],heights[right])
            max = Math.max(temp, max)
            heights[left] < heights[right] ? left++ : right--;
        }
        return max;
    }
}
