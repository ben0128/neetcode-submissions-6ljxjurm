class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let max = Math.max(...piles);
        let min = 1;
        let res = max;
        while (min <= max) {
            let time = 0;
            let each = min + Math.floor((max-min)/2);
            for (const pile of piles) {
                time += Math.ceil(pile/each);
            }
            if (time <= h){
                max = each-1
                res = each;
            } else {
                min = each+1
            }
        }
        return res;
    }
}
