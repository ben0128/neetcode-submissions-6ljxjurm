class Solution {
    /**
     * @param {number[]} stones
     * @return {number}
     */
    lastStoneWeight(stones) {
        while (stones.length > 1) {
            stones.sort((a,b) => a - b);
            const pop1 = stones.pop();
            const pop2 = stones.pop();
            if (pop1 != pop2 ) stones.push(Math.abs(pop1-pop2));
        }
        return stones.length === 1 ? stones[0] : 0;
    }
}
