class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let i = 0, j = numbers.length -1
        while (i<j) {
            let tempSum = numbers[i]+numbers[j]
            if (tempSum === target) return [i+1, j+1]
            if (tempSum < target) i++
            else j--
        }
        return [-1, -1] // 雖然必定會有一組以防萬一還是放一下
    }
}
